from dataclasses import dataclass
from dataclasses_json import dataclass_json

class Event:
    '''Query return a result and do not change the state of a system'''
    pass

@dataclass(frozen=True)
class FileStatsCollected(Event):
    """Информация о файле: имя, размер, путь к файлу"""
    name: str
    size: int
    path: str

@dataclass_json
@dataclass(frozen=True)
class ResourceExplored(Event):
    '''Информация о файле в папке'''
    path: str
    extention: str

# Процесс изменения неймспейса
# event:Start Начало процесса
@dataclass(frozen=True)
class DiscoverAllResourceByExtention(Event):
    '''Вручную создается событие запуска процесса.
        Создаются запросы поиска ресурсов.
        Указывается путь к папке с ресурсами проекта'''
    path: str

# event:Milestone Файл для изменения неймпспейса найден
@dataclass(frozen=True)
class ReplaceUFOS2StudioNamespace(Event):
    '''Запуск команды замены нейсмпейса'''
    path: str

# event:End Конец процесса
@dataclass(frozen=True)
class NamespaceChanged(Event):
    '''Информация о ресурсах, у которых был изменен неймспейс'''
    project_name: str
    formular_name: str
    formular_part_name: str
    formular_part_extention: str