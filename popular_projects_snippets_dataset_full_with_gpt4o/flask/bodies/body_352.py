# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
kwargs["environ_base"] = self._copy_environ(kwargs.get("environ_base", {}))
_l_(22922)
builder = EnvironBuilder(self.application, *args, **kwargs)
_l_(22923)

try:
    _l_(22927)

    aux = builder.get_request()
    _l_(22924)
    exit(aux)
finally:
    _l_(22926)

    builder.close()
    _l_(22925)
