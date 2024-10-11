import unittest.mock # pragma: no cover
import pandas as pd # pragma: no cover

request = unittest.mock.Mock() # pragma: no cover
request.param = pd.Timedelta('10 minutes 7 seconds') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/conftest.py
from l3.Runtime import _l_
"""
    Several variants of Timedelta scalars representing 10 minutes and 7 seconds.
    """
aux = request.param
_l_(6168)
exit(aux)
