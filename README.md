# vote-app 

[![Django CI](https://github.com/cristian-rincon/vote-app/actions/workflows/django.yml/badge.svg)](https://github.com/cristian-rincon/vote-app/actions/workflows/django.yml)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cristianr)

Simple vote app built on top of Django. Currently the frontend layer are built on top of [Bootstrap](https://getbootstrap.com/).

## Instalation

This project currently uses [Poetry](https://python-poetry.org/) as dependency manager, you must install it before install left deps.

```bash
poetry install
```

## Usage

Here is the way to use the development version of the app.

### Step by step commands

```bash
# Build the app
docker-compose up

# Create Superuser
docker exec -it vote-app_web_1 python backend/manage.py createsuperuser
```

## Look and feel

### Home view

![Home view](sample_images/1.png)

### Vote view

![Vote view](sample_images/2.png)

### Results view

![Results view](sample_images/3.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

### Made with &#10084;&#65039; &nbsp;from &#127464;&#127476;
