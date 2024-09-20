# Join Backend

## Installation

python -m venv env
source env/bin/activate # Für Windows: env\Scripts\activate

## Installiere die Abhängigkeiten

pip install -r requirements.txt

## Führe Migrationen durch:

python manage.py makemigrations
python manage.py migrate

## Erstelle einen Superuser für das Admin-Interface:

python manage.py createsuperuser

## Starte den lokalen Entwicklungsserver:

python manage.py runserver
