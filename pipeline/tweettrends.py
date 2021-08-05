# Copyright 2021 @apichick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import apache_beam as beam
from apache_beam.transforms.combiners import TopCombineFn
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import SlidingWindows
import json

def get_tweet_hashtags(tweet):
    for entity in tweet['entities']['hashtags']:
        yield '#%s' % entity['text']  

def format_message(items):
    result = {}
    result['metric'] = 'top10hashtags'
    result['data'] = [ {'hashtag': item[0], 'ocurrences': item[1]} for item in items]
    yield json.dumps(result).encode('utf-8')

def run(tweets_topic, trends_topic, beam_args):

    options = PipelineOptions(beam_args, save_main_session=True, streaming=True)
    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic=tweets_topic)
            | 'Parse JSON' >> beam.Map(json.loads)
            | 'Add timestamp' >> beam.Map(lambda item: beam.window.TimestampedValue(item, int(item['timestamp_ms']) / 1000))
            | 'Apply sliding window' >> beam.WindowInto(SlidingWindows(300, 60))
            | 'Extract hashtags' >> beam.ParDo(get_tweet_hashtags)
            | 'Transform to key-value pairs' >> beam.Map(lambda hashtag: (hashtag, 1))
            | 'Count per key' >> beam.combiners.Count.PerKey()
            | 'Get top 10 hashtags' >> beam.CombineGlobally(TopCombineFn(n=10, key=lambda item: item[1])).without_defaults()
            | 'Format' >> beam.ParDo(format_message)
            | 'Write to Pub/Sub' >> beam.io.WriteToPubSub(topic=trends_topic)
        )
