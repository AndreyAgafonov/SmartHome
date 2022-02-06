#!/bin/bash

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PROJECTSNAME=(
  smarthome
  users
)

cd $SCRIPTDIR/..
WORKDIR=$(pwd)

for PROJECT in ${PROJECTSNAME[@]}; do
  echo "backup $PROJECT project"
  source "$WORKDIR/$PROJECT/scripts/backup_script.sh"
done
