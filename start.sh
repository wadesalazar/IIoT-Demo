#!/bin/bash

cd web/

docker build.

sudo docker images | grep none | grep -oP [a-z0-9]{12}
export containerID=8b234ad701ff

sudo docker run  -p 8081:8080 $containerID





