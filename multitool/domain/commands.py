from dataclasses import dataclass

class Command:
    '''Commands change the state of the system but do not necessary return a value'''
    pass

@dataclass(frozen=True)
class ReplaceUFOS2StudioNamespace(Command):
    path: str

