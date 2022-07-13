from dataclasses import dataclass

# Структура папок
# WORKSPACE_DIR/exp-03-supp/ - папка клонированного гит репозитория
# WORKSPACE_DIR/migration/
#                   exp-03-supp/ - папка импортированного проекта

# Рабочая папка, в которую клонируется гит репозиторий и в которой размещается мигрированный из Студии проект
WORKSPACE_DIR = '../../'
GIT_DIR = f'{WORKSPACE_DIR}ufocc-supp/'
MIG_DIR = f'{WORKSPACE_DIR}migration/OTR/' 
GIT_DOCS_DIR = f'{GIT_DIR}Func/docs/'
MIG_DOCS_DIR = f'{MIG_DIR}Func/docs/'
GIT_LC_DIR = f'{GIT_DIR}Func/config/lifecycles/'
MIG_LC_DIR = f'{MIG_DIR}Func/config/lifecycles/'
NAVIGATION_DIR = f'{WORKSPACE_DIR}migration/OTR/Func/config/sufd-interface/setup/navigation/default.navigation'

UFOS_CORE_METADATA = {
    'workspace': WORKSPACE_DIR,
    'project': f'{WORKSPACE_DIR}ufos-core-metadata/',
    'docs': f'{WORKSPACE_DIR}ufos-core-metadata/Func/docs/',
}

UFOCC_SUPP = {
    'workspace': WORKSPACE_DIR,
    'project': f'{WORKSPACE_DIR}ufocc-supp/',
    'docs': f'{WORKSPACE_DIR}ufocc-supp/Func/docs_cdo/',
}

TSE_SUPP = {
    'workspace': WORKSPACE_DIR,
    'project': f'{WORKSPACE_DIR}tse-supp/',
    'docs': f'{WORKSPACE_DIR}tse-supp/Func/docs/'
}

NSI_SUPP = {
    'workspace': WORKSPACE_DIR,
    'project': f'{WORKSPACE_DIR}nsi-supp/',
    'docs': f'{WORKSPACE_DIR}nsi-supp/Func/docs/',
}

EXP_03_SUPP = {
    'workspace': '../../',
    'project': f'{WORKSPACE_DIR}exp-03-supp/',
    'docs': f'{WORKSPACE_DIR}exp-03-supp/Func/docs/',
}

UFOCC = {
    'workspace': '../../../gerrit/',
    'project': '../../../gerrit/ufocc/',
    'docs': '../../../gerrit/ufocc/Func/docs_cdo/',
}

@dataclass(frozen=True)
class ProjectWorkspace:
    workspace: str = '../../../'
    docs: str = f'{workspace}ufos-core-metadata/Func/docs/'
    project_name: str = docs.split('/')[len(workspace.split('/'))-1]