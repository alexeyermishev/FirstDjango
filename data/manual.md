### Выгрузить данные из БД  

```
python manage.py dumpdata MainApp --indent 4 > ./data/MainApp.json
```  

### Загрузить данные в БД  

```
python manage.py loaddata ./data/MainApp.json
```
