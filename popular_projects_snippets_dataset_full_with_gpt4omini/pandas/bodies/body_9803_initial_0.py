import unittest.mock as mock # pragma: no cover

request = mock.Mock() # pragma: no cover
request.param = 'some_param' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/window/conftest.py
from l3.Runtime import _l_
"""engine and raw keyword arguments for rolling.apply"""
aux = request.param
_l_(9970)
exit(aux)
