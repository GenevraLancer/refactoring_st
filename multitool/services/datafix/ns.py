
from typing import Iterator, TextIO
import re

from multitool.domain import events, commands, queries
from multitool.services import uow

# Сервис ищет NAMESPACES_UFOS в xml дескрипторах на файловой системе и заменяет их на неймспейсы Студии NAMESPACES_STUDIO

NAMESPACES_UFOS = { 'filter': 'http://ufos.otr.ru/schema/document/filter/v1',
                'table': 'http://ufos.otr.ru/schema/document/table/v1',
                'edit': 'http://ufos.otr.ru/schema/document/edit/v1',
                'quickview': 'http://ufos.otr.ru/schema/document/quick-view/v1',
                'dialog': 'http://ufos.otr.ru/schema/document/edit/v1',
                'order': 'http://ufos.otr.ru/schema/document/order/v1',
                'history': 'http://ufos.otr.ru/schema/document/history/v1',
                'table-actions': 'http://ufos.otr.ru/schema/document/table-actions/v1',
                'fill': 'http://ufos.otr.ru/schema/document/filling/v1',
                'print': 'http://ufos.otr.ru/schema/document/print/v1',
                'check': 'http://ufos.otr.ru/schema/document/check/v1',
                'mapping': 'http://ufos.otr.ru/schema/document/mapping/v1'}

NAMESPACES_STUDIO = { 'filter': 'http://www.otr.ru/sufd/document/filter',
                'table': 'http://www.otr.ru/sufd/document/table',
                'edit': 'http://www.otr.ru/sufd/document/viewform',
                'quickview': 'http://www.otr.ru/sufd/document/viewform',
                'dialog': 'http://www.otr.ru/sufd/document/viewform',
                'order': 'http://www.otr.ru/sufd/document/order',
                'history': 'http://www.otr.ru/sufd/document/history',
                'table-actions': 'http://www.otr.ru/sufd/document/table-actions',
                'fill': 'http://www.otr.ru/sufd/document/filling',
                'print': 'http://www.otr.ru/sufd/document/print',
                'check': 'http://www.otr.ru/sufd/document/check',
                'mapping': 'http://www.otr.ru/sufd/document/mapping'}

# Последовательность вызова на шине поисковых запросов и обработчиков
# Последовательность вызова на шине поисковых запросов и команд
# Последовательность вызова событий: начало процесса, вехи процесса, конец процесса
REPLACE_NS_PROCESS = {
    events.DiscoverAllResourceByExtention: [queries.DiscoverAllResourceByExtention], # hand made event lunch a process
    events.ReplaceUFOS2StudioNamespace: [commands.ReplaceUFOS2StudioNamespace], # milestone
    events.NamespaceChanged: None # end process
}

# Генератор событий для всех найденных файлов
def query_all_files_with_ufos_extention(e: events.DiscoverAllResourceByExtention, uow: uow.IUoW) -> Iterator[queries.DiscoverAllResourceByExtention]:
    _path = e.path
    for extention in NAMESPACES_UFOS:
        yield queries.DiscoverAllResourceByExtention(_path, extention)

# Функция сверки и замены неймспейса в файлах, перезаписывает файлы на диске 
class ReplaceNS:
    '''Simple use case to datafix namespaces in files'''

    def __init__(self, uow: uow.IUoW):
        self._uow = uow
    
    def __call__(self, c: commands.ReplaceUFOS2StudioNamespace):
        self._docs_path = c.path
        with self._uow: # Start a ServiceUoW as a context manager
            for event in self.execute():
                self._uow.collect_events(event)
            self._uow.publish_events()

    def _replace_patterns_in_file(self, input_text:str, ns_key:str) -> str:
        replaced_text = re.sub(f'xmlns=\"{NAMESPACES_UFOS[ns_key]}', f'xmlns=\"{NAMESPACES_STUDIO[ns_key]}', input_text)
        replaced_text = re.sub(f'xsi:schemaLocation=\"{NAMESPACES_UFOS[ns_key]}', f'xsi:schemaLocation=\"{NAMESPACES_STUDIO[ns_key]}', replaced_text)
        return replaced_text

    def _replace_file(self, path:str, ns_key:str) -> TextIO:
        with open(path, 'r+', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            text = self._replace_patterns_in_file(text, ns_key)
            f.seek(0)
            f.write(text)
            f.truncate()

    def execute(self) -> Iterator[events.NamespaceChanged]:
        for extention in NAMESPACES_UFOS:
            #for path in crawler.find_resource_path_by_extention(self._docs_path, '.'+extention):
                #self._replace_file(path, extention)
                resource = str(self._docs_path).split('/')[-1]
                yield events.NamespaceChanged(
                    project_name = self._docs_path,
                    formular_name = str(self._docs_path).split('/')[-3],
                    formular_part_name = resource.split('.')[0],
                    formular_part_extention = extention
                )