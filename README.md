# Velo_maksymilian_F

## Django REST API project to manage music hits.

### Features

- Add, update and delete records
- Hits related to artists
- Searchable by `title_url`

## How to run?

```bash
git clone <repository address>
cd hitapi
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## How to test?
Just type "pytest" in terminal. 

## Endpoints:
GET /api/v1/hits/ – list of 20 hits

POST /api/v1/hits/ – add hit

GET /api/v1/hits/<title_url> – specs of hit 

PUT /api/v1/hits/<title_url> – edit hit

DELETE /api/v1/hits/<title_url> – delete hit

## Technologies Used:
* Python 3.13
* Django
* Django Rest Framework
* Pytest

## Author
Maksymilian Florek
