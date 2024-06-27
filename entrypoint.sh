#!/bin/bash

# Executa as migrações
python manage.py migrate --no-input

# Cria o superusuário se não existir
echo "from django.contrib.auth.models import User; User.objects.create_superuser('djangovogue', 'admin@example.com', 'admindjango')" | python manage.py shell

# Inicia o servidor Django
python manage.py runserver 0.0.0.0:8000
