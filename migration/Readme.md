# Программа миграции формуляров, ЖЦ Студии2 в Студию3

## Установка
Клонировать гит проект https://gl-sk-prod.otr.ru/studio/studio-design.git

Задать в ```.env``` файле путь к рабочей папке ```WORKSPACE_PATH```
Например: для Win10, ```WORKSPACE_PATH=E:/kotova.evgenia/gitLab``` (использовать прямые / слэши), для MacOS ```WORKSPACE_PATH=~/gitLab```


Структура рабочей папки, в которую клонируется гит репозиторий и в которой размещается мигрированный из Студии проект
```
WORKSPACE_PATH/exp-03-supp/ - папка клонированного гит репозитория
WORKSPACE_PATH/migration/MSC/ - папка экспортированного из Студии2 проекта
```

## Запуск
Команды в консоли из папки ```studio-design/migration```
```
docker login cr-sk-prod.otr.ru:5005
docker pull cr-sk-prod.otr.ru:5005/studio/studio-design/migration-app:latest
docker-compose up -d
```

Открыть в браузере http://localhost:8800
Открыть файл ```migration.ipynb```

## Проведение миграции
Запустить по очереди ячейки в блокноте ```migration.ipynb```
В разделе **Константы** указать название гит проекта и мигрированного проекта
```
GIT_DIR = f'{WORKSPACE_DIR}exp-03-supp/' - папка клонированного гит репозитория
MIG_DIR = f'{WORKSPACE_DIR}migration/MSC/' - папка экспортированного из Студии проекта
```

## Проверка миграции
Открыть в IDEA гит проект и посмотреть на вкладке Git:Local Changes состав изменений:
1. Изменения в desc, counter, edit, sign-schema
2. Изменения в lc

## Остановка
Команда в консоли из папки ```studio-design/migration```
```
docker-compose down --volumes
```
Если в ```migration.ipynb``` вносились изменения, то чтобы их сохранить и увидеть при следующем запуске приложения, останавливать командой
```
docker-compose down
```