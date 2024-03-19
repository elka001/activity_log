FROM ubuntu:latest
LABEL authors="elzek"

ENTRYPOINT ["top", "-b"]