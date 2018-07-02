#!/usr/bin/env bash
set -e
helm package ./charts/py-healthchecks/ -d ./charts
helm repo index ./charts