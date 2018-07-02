#!/usr/bin/env bash
set -e

rel_path=`dirname $0`/../
repo="quay.io/verygoodsecurity/py-healthchecks"
version=`cat ${rel_path}/src/Version`

docker build --rm=true -t ${repo}:${version} ${rel_path}/src