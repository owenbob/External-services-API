
[![CircleCI](https://circleci.com/gh/owenbob/External-services-API.svg?style=svg)](https://circleci.com/gh/owenbob/External-services-API)
# External-services-API 

## Product overview 
 This is a simple API that calls 

## Development set up
- Check that python 3, pip ,virtualenv and elasticsearch are installed

- Clone   External-services-API   repo and cd into it
    ```
    git clone https://github.com/owenbob/Yummy-Recipes-Django-REST-API.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```

- Run application.
    ```
    cd projects/
    ```
    ```
    python manage.py runserver
    ```
- Run Tests
    ```
    python manage.py test api
    ```
    
    
## Built with 
- Python version  3
- Django
- Django Rest Framework
- Elasticsearch