# Dataflow Flex template

This is the code of the Dataflow Flex Template that has been used for the Beam Summit 2021 [this](https://github.com/apichick/beam-summit-2021-flex-templates-cicd-demo.git) workshop.

## Pre-requisites

The following software needs to be installed in your machine:

* gcloud CLI

## Publishing the Dataflow template and using it to run a pipeline

1. Create a project in Google Cloud.

2. Clone this repository

        git clone git@github.com:apichick/beam-summit-2021-flex-template.git

2. Log in to Google Cloud

        gcloud auth login

3. Edit the settings.sh file and initialize the REGION and PROJECT_ID environment variables.

4. Run the following command to publish the template:

        ./deploy.sh

5. Run the following command to create a pipeline from the template

        ./run.sh


