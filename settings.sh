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

#!/bin/bash

export REGION="europe-west1"
export PROJECT_ID=$1
export BUCKET=${PROJECT_ID}
export TEMPLATE_IMAGE="gcr.io/${PROJECT_ID}/tweettrends:latest"
export TEMPLATE_PATH="gs://${BUCKET}/dataflow/templates/tweettrends.json"
export TWEETS_TOPIC="projects/${PROJECT_ID}/topics/tweets"
export TRENDS_TOPIC="projects/${PROJECT_ID}/topics/trends"
