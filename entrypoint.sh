#!/bin/sh
# entrypoint.sh
flask db upgrade || true
exec "$@"
