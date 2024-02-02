# pollpal-api

A user-friendly backend solution for creating and participating in polls and surveys.

## Tech stack

- Python 3.11.4
- Django 4.2
- Django REST Framework 3.14

## Endpoints

**Get all polls or a single one:**

```
api/v1/polls/
api/v1/polls/<int:pk>/
```

**example result:**

```
{
    "id": 1,
    "options": [
        {
            "id": 1,
            "text": "Option one",
            "votes_count": 2,
            "percentage": 66.67
        },
        {
            "id": 2,
            "text": "Option two",
            "votes_count": 1,
            "percentage": 33.33
        }
    ],
    "question": "Better option ?",
    "created_at": "2024-02-02T16:47:42.834664Z",
    "expires_at": "2024-02-06T16:47:40Z"
}
```

**Create a poll:**
Options should be provided as a list of individual options like: **{'text': 'my option'}**

```
api/v1/ polls/create/
```

**Vote on an option:**
The vote is validated so that a user can't duplicate votes on the same poll

```
api/v1/ polls/vote/
```

## Local setup guide

**Clone repo and install necessary dependencies:**

```
git clone https://github.com/FPorucznik/pollpal-api.git
cd pollpal-api
pip install -r requirements.txt
```

**Migrate database:**

```
cd pollpal-api
python ./manage.py migrate
```

**Run app:**

```
python ./manage.py runserver
```
