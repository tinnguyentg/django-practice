from json import JSONDecodeError
from typing import Dict, Type

import requests
from django.conf import settings


class Oxford:
    """Make request with required headers to Oxford Dictionary API"""

    BASE = "https://od-api.oxforddictionaries.com/api/v2"
    HEADERS = {
        "app_id": settings.OXFORD_APP_ID,
        "app_key": settings.OXFORD_APP_KEY,
    }

    def __init__(self, end_point: str):
        self._url = self.BASE + end_point

    def get(self) -> Dict:
        """Make request

        If request succeed, return it's json data,
        otherwise also try return it's json data or response.text
        """
        response = requests.get(self.url, headers=self.headers)

        if response.ok:
            return response.json()
        else:
            try:
                return response.json()
            except JSONDecodeError:
                return {"msg": response.text}

    @property
    def url(self) -> str:
        return self._url

    @property
    def headers(self) -> Dict:
        return self.HEADERS


class Entries:
    def __init__(self, word: str, source: str = "en-us"):
        self._endpoint = f"/entries/{source}/{word}"
        self._oxford = Oxford(self.endpoint)

    def result(self) -> Dict:
        return self.oxford.get()

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def oxford(self) -> Type[Oxford]:
        return self._oxford


class Lemmas:
    def __init__(self, word: str, source: str = "en"):
        self._endpoint = f"/lemmas/{source}/{word}"
        self._oxford = Oxford(self.endpoint)

    def result(self) -> Dict:
        return self.oxford.get()

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def oxford(self) -> Type[Oxford]:
        return self._oxford
