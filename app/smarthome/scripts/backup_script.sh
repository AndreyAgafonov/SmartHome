#!/bin/bash
#set -e
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
TIMESTAMP=$(date +'%Y.%m.%d_%H-%M-%S')
PROJECTNAME=smarthome

echo $TIMESTAMP
cd $SCRIPTDIR/../..
WORKDIR=$(pwd)
echo $WORKDIR
echo $SCRIPTDIR

python3 manage.py dumpdata smarthome.RoomType >RoomType.json
python3 manage.py dumpdata smarthome.Rooms >Rooms.json
python3 manage.py dumpdata smarthome.SensorsDataType >SensorsDataType.json
python3 manage.py dumpdata smarthome.SensorsType >SensorsType.json
python3 manage.py dumpdata smarthome.SensorsLocate >SensorsLocate.json
python3 manage.py dumpdata smarthome.SensorsData >SensorsData.json
#python3 manage.py dumpdata smarthome.SettingsCategory > SettingsCategory.json
python3 manage.py dumpdata smarthome.SettingsSections >SettingsSections.json
python3 manage.py dumpdata smarthome.SettingsType >SettingsType.json
python3 manage.py dumpdata smarthome.Settings >Settings.json

mkdir -p $PROJECTNAME/fixtures/$TIMESTAMP
mv *.json $PROJECTNAME/fixtures/$TIMESTAMP
rm $PROJECTNAME/fixtures/latest
ln -fs $WORKDIR/$PROJECTNAME/fixtures/$TIMESTAMP $PROJECTNAME/fixtures/latest
