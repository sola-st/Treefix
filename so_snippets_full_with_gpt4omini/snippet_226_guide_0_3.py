# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
from l3.Runtime import _l_
def POST_request():
    _l_(1654)

    with open("FILE PATH", "r") as data:
        _l_(1651)

        JSON_Body = data.read()
        _l_(1650)
    response = requests.post(url="URL", data=JSON_Body)
    _l_(1652)
    assert response.status_code == 200
    _l_(1653)

