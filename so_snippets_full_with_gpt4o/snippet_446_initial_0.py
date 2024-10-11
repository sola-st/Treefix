from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
type('Mock', (object,), {'run': lambda self, host, port: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
from l3.Runtime import _l_
try:
    import os
    _l_(13885)

except ImportError:
    pass

if __name__ == "__main__":
    _l_(13888)

    port = int(os.environ.get("PORT", 5000))
    _l_(13886)
    app.run(host='0.0.0.0', port=port)
    _l_(13887)

