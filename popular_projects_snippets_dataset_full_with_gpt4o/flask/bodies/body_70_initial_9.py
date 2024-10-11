from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.config["MAX_CONTENT_LENGTH"] = 1048576 # pragma: no cover
current_app = app # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
"""Read-only view of the ``MAX_CONTENT_LENGTH`` config key."""
if current_app:
    _l_(22830)

    aux = current_app.config["MAX_CONTENT_LENGTH"]
    _l_(22828)
    exit(aux)
else:
    aux = None
    _l_(22829)
    exit(aux)
