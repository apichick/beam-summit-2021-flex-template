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
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that, equal_to
from pipeline.tweettrends import get_tweet_hashtags

TWEETS = [{
    "created_at": "Thu Aug 05 16:44:35 +0000 2021",
    "id": 1423324062764478464,
    "id_str": "1423324062764478464",
    "text": "Enjoy the calm before storm. #ITsPrecious",
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "truncated": False,
    "in_reply_to_status_id": None,
    "in_reply_to_status_id_str": None,
    "in_reply_to_user_id": None,
    "in_reply_to_user_id_str": None,
    "in_reply_to_screen_name": None,
    "user": {
        "id": 10855182,
        "id_str": "10855182",
        "name": "steketee",
        "screen_name": "steketee",
        "location": "nyc + the \u2601\ufe0f",
        "url": "https://linkedin.com/in/paulsteketee",
        "description": "Proud Husband & Father of 2 w @eelain212, Founder & MD @Addressomo, Average & Rusty Tennis Player, @Instapour CEO; #Startups #Advisor #Investor, & Fan of You!",
        "translator_type": "none",
        "protected": False,
        "verified": False,
        "followers_count": 1630,
        "friends_count": 1563,
        "listed_count": 102,
        "favourites_count": 19269,
        "statuses_count": 33867,
        "created_at": "Tue Dec 04 23:42:23 +0000 2007",
        "utc_offset": None,
        "time_zone": None,
        "geo_enabled": True,
        "lang": None,
        "contributors_enabled": False,
        "is_translator": False,
        "profile_background_color": "C0DEED",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
        "profile_background_tile": False,
        "profile_link_color": "0FB300",
        "profile_sidebar_border_color": "C0DEED",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_text_color": "333333",
        "profile_use_background_image": True,
        "profile_image_url": "http://pbs.twimg.com/profile_images/480823481614229504/5kS_9XBR_normal.jpeg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/480823481614229504/5kS_9XBR_normal.jpeg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/10855182/1411278364",
        "default_profile": False,
        "default_profile_image": False,
        "following": None,
        "follow_request_sent": None,
        "notifications": None,
        "withheld_in_countries": []
    },
    "geo": None,
    "coordinates": None,
    "place": {
        "id": "01a9a39529b27f36",
        "url": "https://api.twitter.com/1.1/geo/id/01a9a39529b27f36.json",
        "place_type": "city",
        "name": "Manhattan",
        "full_name": "Manhattan, NY",
        "country_code": "US",
        "country": "United States",
        "bounding_box": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        -74.026675,
                        40.683935
                    ],
                    [
                        -74.026675,
                        40.877483
                    ],
                    [
                        -73.910408,
                        40.877483
                    ],
                    [
                        -73.910408,
                        40.683935
                    ]
                ]
            ]
        },
        "attributes": {}
    },
    "contributors": None,
    "is_quote_status": False,
    "quote_count": 0,
    "reply_count": 0,
    "retweet_count": 0,
    "favorite_count": 0,
    "entities": {
        "hashtags": [
            {
                "text": "ITsPrecious",
                "indices": [
                    29,
                    41
                ]
            }
        ],
        "urls": [],
        "user_mentions": [],
        "symbols": []
    },
    "favorited": False,
    "retweeted": False,
    "filter_level": "low",
    "lang": "en",
    "timestamp_ms": "1628181875302"
}];

HASHTAGS = [ 
    "#ITsPrecious"
];

def test_get_tweet_entities():
    with TestPipeline() as p:
        input = p | 'Create tweets' >> beam.Create(TWEETS)
        output = input | 'Get hashtags' >> beam.ParDo(get_tweet_hashtags)
        assert_that(output, equal_to(HASHTAGS), label='CheckOutput')
