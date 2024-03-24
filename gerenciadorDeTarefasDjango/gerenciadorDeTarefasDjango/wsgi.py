"""
WSGI config for gerenciadorDeTarefasDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

'''import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciadorDeTarefasDjango.settings')

application = get_wsgi_application()'''

import os
import sys

# Adicione o diretório do seu projeto Django ao sys.path
path = '/home/leilinhasds/Gerenciador-de-Tarefas-programa-Match-IBM/gerenciadorDeTarefasDjango/gerenciadorDeTarefasDjango'
if path not in sys.path:
    sys.path.append(path)

# Configure as configurações do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'gerenciadorDeTarefasDjango.settings'

# Obtenha a aplicação WSGI do Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

