#!/bin/bash

docker login repo.treescale.com --username thomas_michelet --password Rudeboy788?788
ansible-playbook -i inventories/production deploy.yml