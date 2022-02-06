#!/bin/bash
#set -e
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
TIMESTAMP=$(date +'%Y.%m.%d_%H-%M-%S')
PROJECTNAME=users

echo $TIMESTAMP
cd $SCRIPTDIR/../..
WORKDIR=$(pwd)
echo $WORKDIR

python3 manage.py dumpdata users.user >adminUser.json

mkdir -p $PROJECTNAME/fixtures/$TIMESTAMP
mv *.json $PROJECTNAME/fixtures/$TIMESTAMP
rm $PROJECTNAME/fixtures/latest
ln -fs $WORKDIR/$PROJECTNAME/fixtures/$TIMESTAMP $PROJECTNAME/fixtures/latest
