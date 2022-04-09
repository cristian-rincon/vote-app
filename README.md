# vote-app API

[![Django CI](https://github.com/cristian-rincon/vote-app/actions/workflows/django.yml/badge.svg)](https://github.com/cristian-rincon/vote-app/actions/workflows/django.yml) [![codecov](https://codecov.io/gh/cristian-rincon/vote-app/branch/main/graph/badge.svg?token=KKDK1KJR8Y)](https://codecov.io/gh/cristian-rincon/vote-app)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cristianr)

Simple vote api built on top of [Django Rest Framework](https://www.django-rest-framework.org/).

- [vote-app API](#vote-app-api)
  - [API Spec](#api-spec)
  - [Instalation](#instalation)
  - [What's in this project?](#whats-in-this-project)
    - [Important files](#important-files)
  - [Usage](#usage)
    - [Step by step commands](#step-by-step-commands)
      - [1. Start the server and create the admin user](#1-start-the-server-and-create-the-admin-user)
  - [Contributing](#contributing)
  - [License](#license)
    - [Made with &#10084;&#65039; &nbsp;from &#127464;&#127476;](#made-with-️-from-)

## API Spec

You can find the API Spec in the following endpoint: `/openapi`

## Instalation

This project currently uses [Poetry](https://python-poetry.org/) as dependency manager, you must install it before install left deps.

```bash
poetry install
```

## What's in this project?

This solution is containarized with Docker, it's a good practice to use it. The docker-compose file includes `postgres` database(to be used in development), `web` container (with the api), and `pgadmin` container (to manage the database). This solution is not ready for production, but you can use it in development.

### Important files

`docker-compose.yml` file is the main config file for the project, you can find it in the root of the project.
`Dockerfile` is the main Dockerfile for the project, you can find it in the root of the project.
`pyproject.toml` is the poetry config file for the project, you can find it in the root of the project.
`poetry.lock` is the poetry lock file for the project, you can find it in the root of the project.

## Usage

Here is the way to use the development version of the app.

### Step by step commands

#### 1. Start the server and create the admin user

```bash
# Build the app
docker-compose up

# Create Superuser
docker exec -it vote-app_web_1 python backend/manage.py createsuperuser
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

### Made with &#10084;&#65039; &nbsp;from &#127464;&#127476;
