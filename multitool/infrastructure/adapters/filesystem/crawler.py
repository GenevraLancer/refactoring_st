from typing import Iterable
from pathlib import Path
from multitool.domain import events, commands, queries
from multitool.services import uow
from multitool import config


def find_resource_stats_by_extention(path: str, extention: str) -> Iterable[events.FileStatsCollected]:
    """ Функция рекурсивного поиска файлов заданного расширения во вложенных папках
        Находит путь файла, имя файла и размер
        Примеры расширения файлов .desc, .edit
        Возвращает кортеж Название файла, размер, путь файла"""
    files_path = Path(path)

    with uow: #start a ServiceUoW as a context manager, implement resource management patterns
        for file in files_path.glob(f"**/*{extention}"):
            if file.is_file():
                uow.collect_events(events.FileStatsCollected(
                    name = file.name, 
                    size = file.stat().st_size, 
                    path = str(file),
                    ))
        uow.publish_events()

def find_resource_path_by_extention(query: queries.DiscoverAllResourceByExtention, uow: uow.IUoW) -> Iterable[events.ReplaceUFOS2StudioNamespace]:
    """ Функция рекурсивного поиска файлов заданного расширения во вложенных папках
        Находит путь файла, имя файла и размер
        Примеры расширения файлов .desc, .edit  
        Возвращает путь файла"""
    
    files_path = Path(query.path)

    with uow: #start a ServiceUoW as a context manager
        for file in files_path.glob(f"**/*{query.extention}"):
            if file.is_file():
                uow.collect_events(events.ReplaceUFOS2StudioNamespace(
                    path = str(file)
                ))
        uow.publish_events()
        

def find_resources(query: queries.DiscoverProjectResources, uow: uow.IUoW) -> Iterable[events.ResourceExplored]:
    path = Path(query.folder)

    with uow: #start a ServiceUoW as a context manager
        for file in path.glob(f"**/*"):
            if file.is_file():
                resource = str(file).split('/')[-1]
                uow.collect_events(events.ResourceExplored(
                    path = str(file),
                    extention = resource.split('.')[-1]
                ))
        uow.publish_events()