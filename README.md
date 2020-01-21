# Damage

This is an unpublished Slack Application.

Slack Application that takes Monzo IFTTT posts to a Slack channel and totals the amount in the messages for the previous day. It posts the total as the days Damage.

## Tech Stack

It is hosted by AWS Lambda. The function is triggered daily by an AWS Event Rule. It is deployed using a local GitHub Action on push to master.

### Environment Variables

The following variables are provided to the function when it is deployed, the values are stored in GitHub Secrets.

|Variable|Description|
|-|-|
|SLACK_CHANNEL|The ID of the Slack channel to read messages from.|
|SLACK_OAUTH|The OAuth token for the Slack App.|
|SLACK_WEBHOOK|The webhook URL to post messages to as the Damage App.|
