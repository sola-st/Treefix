class Request: # pragma: no cover
    def __init__(self, url: str, method: str): # pragma: no cover
        self.url = url # pragma: no cover
        self.method = method # pragma: no cover
class App: # pragma: no cover
    def __init__(self, name: str): # pragma: no cover
        self.name = name # pragma: no cover

self = type('Mock', (object,), { # pragma: no cover
    'request': Request('http://example.com', 'GET'), # pragma: no cover
    'app': App('ExampleApp') # pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
aux = (
    f"<{type(self).__name__} {self.request.url!r}"
    f" [{self.request.method}] of {self.app.name}>"
)
_l_(19372)
exit(aux)
