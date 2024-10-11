import pandas as pd # pragma: no cover

request = type('Mock', (object,), {'param': [pd.Timedelta('10 minutes 7 seconds'), pd.Timedelta(minutes=10, seconds=7), pd.Timedelta(minutes=10) + pd.Timedelta(seconds=7)]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/conftest.py
from l3.Runtime import _l_
"""
    Several variants of Timedelta scalars representing 10 minutes and 7 seconds.
    """
aux = request.param
_l_(18088)
exit(aux)
