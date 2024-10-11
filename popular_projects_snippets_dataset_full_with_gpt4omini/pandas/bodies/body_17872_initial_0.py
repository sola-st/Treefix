from unittest.mock import Mock # pragma: no cover

request = Mock() # pragma: no cover
request.param = 'exit' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/util/conftest.py
from l3.Runtime import _l_
aux = request.param
_l_(10448)
exit(aux)
