#!/usr/bin/env bash

set -e

uwsgi --strict --ini /app/uwsgi/uwsgi.ini
