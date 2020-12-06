from typing import Any

import click
import requests

API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str = "en") -> Any:
    try:
        with requests.get(API_URL.format(language=language)) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
