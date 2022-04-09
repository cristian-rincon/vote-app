#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

cd backend && poetry run pytest --cov --cov-report xml:coverage.xml