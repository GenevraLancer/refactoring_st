from multitool.domain import events, queries
from typing import Iterator, List

class IUoW:
    '''Abstract interface for unit of work patern'''
    pass

class ServiceUoW(IUoW):
    '''New unit of work will collect a list of events for each handler.
        After each handler finishes, it collect any new events that have been generated and add them to the queue'''
    def __init__(self):
        self._events = [] # type: List[events.Event]
        self.executed = False
    
    def __enter__(self) -> IUoW:
        return self

    def __exit__(self, *args):
        pass

    def collect_events(self, event: events.Event) -> List[events.Event]:
        self._events.append(event)

    def publish_events(self) -> Iterator[events.Event]:
        while self._events:
            yield self._events.pop(0)
        else: 
            self.executed = True