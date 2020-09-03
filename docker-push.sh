#!/bin/bash

docker build -t "repo.treescale.com/thomas_michelet/uniroulotte" .
echo "$DOCKER_PASSWORD" | docker login --username "thomas_michelet" --password-stdin repo.treescale.com
docker push "repo.treescale.com/thomas_michelet/uniroulotte"
