import logging
from typing import Callable, Dict, List, Union, Type
from multitool.domain import commands, events, queries
from multitool.services import uow

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

Message = Union[commands.Command, events.Event, queries.Query]

class Bus:
    '''Bus routes commands, queries or events to one or more handlers'''
    def __init__(
        self,
        uow: uow.IUoW,
        event_handlers: Dict[Type[events.Event], List[Callable]],
        command_handlers: Dict[Type[commands.Command], Callable],
        query_handlers: Dict[Type[queries.Query], Callable]
    ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers
        self.query_handlers = query_handlers

    def execute(self, message: Message):
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)
            if message:
                if isinstance(message, events.Event):
                    self._handle_event(message)
                elif isinstance(message, commands.Command):
                    self._handle_command(message)
                elif isinstance(message, queries.Query):
                    self._handle_query(message)
                else:
                    raise Exception(f"{message} was not an Event, Command or Query")

    def _handle_event(self, event: events.Event):
        logger.info("handling event %s", event)
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug("handling event %s with handler %s", event, handler)
                handler(event, self.uow)
                self.queue.extend(self.uow.publish_events())
            except Exception:
                logger.exception("Exception handling event %s", event)
                continue

    def _handle_command(self, command: commands.Command):
        logger.info("handling command %s", command)
        try:
            handler = self.command_handlers[type(command)]
            handler(command, self.uow)
            self.queue.extend(self.uow.publish_events())
        except Exception:
            logger.exception("Exception handling command %s", command)
            raise
    
    def _handle_query(self, query: queries.Query):
        logger.info("handling query %s", query)
        try:
            handler = self.query_handlers[type(query)]
            handler(query, self.uow)
            self.queue.extend(self.uow.publish_events())
        except Exception:
            logger.exception("Exception handling query %s", query)
            raise