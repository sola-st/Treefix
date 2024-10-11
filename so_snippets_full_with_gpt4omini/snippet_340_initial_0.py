from flask import Flask # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
from l3.Runtime import _l_
app = Flask(__name__, static_url_path='/static')
_l_(2415)


