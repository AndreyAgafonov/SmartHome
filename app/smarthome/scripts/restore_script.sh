#!/bin/bash
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
PROJECTNAME=smarthome

#echo $TIMESTAMP
cd $SCRIPTDIR/../..
WORKDIR=$(pwd)
echo $WORKDIR

#rm $WORKDIR/db.sqlite3
#find $WORKDIR/$PROJECTNAME/migrations/ -type f -regex ".*[0-9].*\.py$" -exec rm -rf {} \;
#
#python3 manage.py makemigrations
#python3 manage.py migrate

python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/RoomType.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/Rooms.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/SensorsDataType.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/SensorsType.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/SensorsLocate.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/SensorsData.json
#python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/SettingsCategory.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/SettingsSections.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/SettingsType.json
python3 manage.py loaddata $WORKDIR/$PROJECTNAME/fixtures/latest/Settings.json
