from dataclasses import dataclass
from multitool import config


class Query:
    '''Query return a data view and do not change the state of a system'''
    pass

@dataclass
class DiscoverProjectResources(Query):
    folder: str

@dataclass
class DiscoverAllResourceByExtention(Query):
    path: str
    extention: str

@dataclass
class DiscoverUFOSResourceByExtention(Query):
    path: str