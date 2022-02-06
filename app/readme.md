преследжую концепцию - сделать все на распберри или ардуино.
пока все бесплатно
### Как запустить проект
должно быть установлено
- окорудение python3.9
- django
- pillow
```bash
python3 -m pip install --upgrade pip
pip3 install --upgrade --force-reinstall  -r scripts/requirements.txt
```
  Прогоняем миграции в нашей базе:


### Как подготовить базу.
  команда создает миграцию - например создание модели бд.
 ```bash
 python3 manage.py makemigrations
 ```

```bash
python3 manage.py migrate
```


### Как запустить миграции


### как вручную запустить команды\ создать записи в бд
Заходим в консоль нашего проекта 
```bash
python manage.py shell
```
Или через pythonConsole -сразу набираем импорт необходимого проекта.

Пример:
добавить в  список всех типов датчиков новый тип
```python3
from smarthome.models import SensorsDataType
cat = SensorsDataType(name= 'temperature
                            ', description = 'test')
cat.save()
```

Способ 2
```python3
from smarthome.models import SensorsDataType
SensorsDataType.objects.create(name='vlagnost\'')
```

Получить все объекты из указанного класса:
```python
from smarthome.models import SensorsDataType
SensorsDataType.objects.all()
```

Получить объекты по фильтру из указанного класса:

1. 
```python
from smarthome.models import SensorsDataType
SensorsDataType.objects.filter(name='temperature')
```
2.
```python
from smarthome.models import SensorsDataType
cat = SensorsDataType.objects.get(id=1)
cat
```

### как создать стандартного пользователя ( первый запуск )
```bash
 python3 manage.py createsuperuser
 ```



dump fixtures
```bash
python3 manage.py dumpdata smarthome.RoomType > RoomType.json
python3 manage.py dumpdata smarthome.Rooms > Rooms.json
python3 manage.py dumpdata smarthome.SensorsDataType > SensorsDataType.json
python3 manage.py dumpdata smarthome.SensorsType > SensorsType.json
python3 manage.py dumpdata smarthome.SensorsLocate > SensorsLocate.json
python3 manage.py dumpdata smarthome.SensorsData > SensorsData.json
python3 manage.py dumpdata auth.user > adminUser.json
```

```bash
python3 manage.py loaddata smarthome/fixtures/RoomType.json
python3 manage.py loaddata smarthome/fixtures/Rooms.json
python3 manage.py loaddata smarthome/fixtures/SensorsDataType.json
python3 manage.py loaddata smarthome/fixtures/SensorsType.json
python3 manage.py loaddata smarthome/fixtures/SensorsLocate.json
python3 manage.py loaddata smarthome/fixtures/SensorsData.json
python3 manage.py loaddata adminUser.json
```




