#!/bin/bash

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PROJECTSNAME=(
  smarthome
  users
)

cd $SCRIPTDIR/..
WORKDIR=$(pwd)

rm $WORKDIR/db.sqlite3
for PROJECT in ${PROJECTSNAME[@]}; do
  find $WORKDIR/$PROJECT/migrations/ -type f -regex ".*[0-9].*\.py$" -exec rm -rf {} \;
done

python3 manage.py makemigrations
python3 manage.py migrate

for PROJECT in ${PROJECTSNAME[@]}; do
  echo "Restore $PROJECT project"
  source "$WORKDIR/$PROJECT/scripts/restore_script.sh"
done
