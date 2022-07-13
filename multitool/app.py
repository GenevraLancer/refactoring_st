import logging
from multitool.services import messagebus, handlers, uow
from multitool.services.datafix import ns
from multitool.domain import queries, commands, events
from multitool import config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

multitool_bus = messagebus.Bus(
    uow = uow.ServiceUoW(), 
    event_handlers= handlers.EVENT_HANDLERS, 
    command_handlers= handlers.COMMAND_HANDLERS, 
    query_handlers= handlers.QUERY_HANDLERS)


# Change namespace process
def change_namespace_process(bus: messagebus.Bus = multitool_bus):
# Step1. Create handmade event
    event = events.DiscoverAllResourceByExtention(path=config.UFOS_CORE_METADATA['docs'])
    logging.info("handling handmade start event %s with path %s", event, event.path)
    stream_ns = [bus.execute(query) for query in ns.query_all_files_with_ufos_extention(event, bus.uow)]

# Step2. Lunch automate by handlers.EVENT_HANDLERS[events.ReplaceUFOS2StudioNamespace]
change_namespace_process()

# start simple query
# multitool_bus.execute(queries.DiscoverProjectResources(folder=config.UFOCC['docs']))

# start simple query
# multitool_bus.execute(queries.DiscoverAllResourceByExtention(path=config.UFOCC['docs'], extention='desc'))

# multitool_bus.execute(commands.ReplaceUFOS2StudioNamespace(path=config.UFOS_CORE_METADATA['docs']))