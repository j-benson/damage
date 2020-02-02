#!/bin/bash

export AWS_DEFAULT_REGION="eu-west-1"
export AWS_ACCESS_KEY_ID=$INPUT_AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$INPUT_AWS_SECRET_ACCESS_KEY

sam build
sam deploy --stack-name Damage-production \
  --s3-bucket sam.damage.bensonj.uk \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    SlackChannel=$INPUT_SLACK_CHANNEL \
    SlackOAuth=$INPUT_SLACK_OAUTH \
    SlackWebhook=$INPUT_SLACK_WEBHOOK
