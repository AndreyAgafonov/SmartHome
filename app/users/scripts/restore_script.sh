#!/bin/bash

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
PROJECTNAME=users

echo $TIMESTAMP
cd $SCRIPTDIR/../..
WORKDIR=$(pwd)
echo $WORKDIR

#rm $WORKDIR/../../db.sqlite3
#find $WORKDIR/$PROJECTNAME/migrations/ -type f -regex ".*[0-9].*\.py$" -exec rm -rf {} \;


#python3 manage.py makemigrations
#python3 manage.py migrate

python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/adminUser.json
