#!/bin/bash
echo "Construyendo el proyecto..."
python3 -m pip install -r requirements.txt
echo "Recolectando archivos estáticos..."
python3 manage.py collectstatic --noinput --clear
echo "Aplicando migraciones a Supabase..."
python3 manage.py migrate