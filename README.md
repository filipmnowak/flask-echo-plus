# flask-echo-plus

Simple, "dockerized" Flask echo app with some extras

## Variables

`FLASK_ECHO_PLUS_REPO` - Docker image name base.
`FLASK_ECHO_PLUS_VERSION` - Docker image version.

### Internal

`ECHO_SUCCESS_RATIO` - Ratio of successfull HTTP responses to 100 responses. Default: 100.
`FLASK_ECHO_PLUS_NAME` - Container name and hostname.

## Build

```sh
export FLASK_ECHO_PLUS_REPO='flask-echo-plus'
export FLASK_ECHO_PLUS_VERSION='v0.1a'

sudo docker build --rm --no-cache -f Dockerfile -t ${FLASK_ECHO_PLUS_REPO}:${FLASK_ECHO_PLUS_VERSION} .
```

## Run

```sh
export ECHO_SUCCESS_RATIO=25
export FLASK_ECHO_PLUS_NAME=${FLASK_ECHO_PLUS_REPO}-001

sudo docker run --rm -d -p 8080:8080 \
  --env ECHO_SUCCESS_RATIO=${ECHO_SUCCESS_RATIO} \
  --hostname ${FLASK_ECHO_PLUS_NAME} \
  --name ${FLASK_ECHO_PLUS_NAME} \
${FLASK_ECHO_PLUS_REPO}:${FLASK_ECHO_PLUS_VERSION}
```
