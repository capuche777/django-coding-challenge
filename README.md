![Static Badge](https://img.shields.io/badge/-3.11.9-000?style=flat&logo=python&logoColor=blue&label=Python&labelColor=000&color=blue)
![Static Badge](https://img.shields.io/badge/-5.0-000?style=flat&logo=django&logoColor=blue&label=Django&labelColor=000&color=blue)

# Django Coding Challenge

## Setup

Clone this repository using GIT.

## Using Docker (Recommended)

You will need Docker installed on your computer. After cloning the repo, simply run:

```shell
docker compose up -d
```

For older versions, use:

```shell
docker-compose up -d
```

To run tests manually:

```shell
docker exec -it nimblestore_dev pytest
```

## Using Python Environment

After cloning the repo:

1. **Create Environment:**

    ```shell
    python -m venv venv
    ```

2. **Activate Environment:**

    - On macOS/Linux:
    
        ```shell
        source venv/bin/activate
        ```

    - On Windows:
    
        ```shell
        .\venv\Scripts\activate
        ```

3. **Install Requirements:**

    ```shell
    pip install -r ./nimblestore/requirements.txt
    ```
   
4. **Navigate to Project Folder:**

    ```shell
    cd ./nimblestore/
    ```
   
5. **Create Superuser:**

    ```shell
    python manage.py --settings=nimblestore.settings.dev createsuperuser
    ```

6. **Run Server:**

    ```shell
    python manage.py runserver --settings=nimblestore.settings.dev
    ```

To run tests manually from root folder:

```shell
pytest ./nimblestore/
```

### Notes:
1. DB is included just for testings purpose.
2. production environment is not introduced in settings because this will not be deployed to production.
