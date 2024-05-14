# __init__.py é um arquivo especial que indica ao Python que o diretório que ele está contido é um pacote.
# Isso significa que ele pode ser importado como um módulo.
# Neste caso, o arquivo __init__.py importa o módulo conta do pacote ContaManagment.
# Mais informações em: https://docs.python.org/3/tutorial/modules.html#packages

from .conta import *