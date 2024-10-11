import requests # pragma: no cover
import sys # pragma: no cover
import types # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
from l3.Runtime import _l_
def POST_request():
    _l_(13319)

    with open("FILE PATH", "r") as data:
        _l_(13316)

        JSON_Body = data.read()
        _l_(13315)
    response = requests.post(url="URL", data=JSON_Body)
    _l_(13317)
    assert response.status_code == 200
    _l_(13318)

