from dataclasses import asdict

from multitool.domain import events, commands, queries
from multitool.services import uow
from multitool.infrastructure.adapters.filesystem import crawler
from multitool.services.datafix import ns
from multitool import config

def start_replace_namespace_in_files(
        event: events.ReplaceUFOS2StudioNamespace, 
        uow: uow.IUoW
):
    with uow:
        uow.collect_events(commands.ReplaceUFOS2StudioNamespace(event.path))
        uow.publish_events()


# type: Dict[Type[events.Event], List[Callable]]
# События сообщают об этапах выполнения команд или запросов. Содержат необходимую информацию.
# У одного события один и более слушателей handlers
# lambda создает inline partitial функции, используется для передачи доп параметров и dependency injection
# https://stackoverflow.com/questions/51286748/make-the-python-json-encoder-support-pythons-new-dataclasses  форматы вывода для event
EVENT_HANDLERS = {
    # events.NamespaceChanged: [lambda e, uow: print(e.__dict__)],
    # events.FileStatsCollected: [lambda e, uow: print(e.to_json())], 
    events.ResourceExplored: [lambda e, uow: print(e.__dict__)],
    events.ReplaceUFOS2StudioNamespace: [lambda e, uow: start_replace_namespace_in_files(e, uow)]
}

# type: Dict[Type[commands.Command], Callable]
# Команды выполняют запись информации в систему/репозиторий. 
# У одной команды один слушатель handler
COMMAND_HANDLERS = {
    commands.ReplaceUFOS2StudioNamespace: lambda c, uow: ns.ReplaceNS(uow)(c) # (uow) передается в конструктор ns.ReplaceNS.__init__, команда (c) передается в функцию ns.ReplaceNS.__call__
}

# type: Dict[Type[queries.Query], Callable]
# Запросы возвращают информацию в нужном для просмотра представлении
# У одного запроса один слушатель handler
QUERY_HANDLERS = {
    queries.DiscoverProjectResources: lambda q, uow: crawler.find_resources(q, uow),
    queries.DiscoverAllResourceByExtention: lambda q, uow: crawler.find_resource_path_by_extention(q, uow),
    # queries.DiscoverUFOSResourceByExtention: lambda q, uow: ns.QueryAllFilesWithUFOSExtention(uow)(q)
}