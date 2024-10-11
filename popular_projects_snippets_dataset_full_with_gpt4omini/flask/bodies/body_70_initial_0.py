from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
current_app = app # pragma: no cover
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
"""Read-only view of the ``MAX_CONTENT_LENGTH`` config key."""
if current_app:
    _l_(7692)

    aux = current_app.config["MAX_CONTENT_LENGTH"]
    _l_(7690)
    exit(aux)
else:
    aux = None
    _l_(7691)
    exit(aux)
