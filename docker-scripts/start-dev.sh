#!/bin/bash
cd ..

docker compose -f docker-compose-dev.yml build  && docker compose -f docker-compose-dev.yml up --watch