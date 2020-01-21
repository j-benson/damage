FROM python:3.7-slim-buster

RUN pip3 install aws-sam-cli

ENTRYPOINT [ "./.github/actions/deploy/entrypoint.sh" ]
