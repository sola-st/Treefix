# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
aux = (
    f"<{type(self).__name__} {self.request.url!r}"
    f" [{self.request.method}] of {self.app.name}>"
)
_l_(8238)
exit(aux)
