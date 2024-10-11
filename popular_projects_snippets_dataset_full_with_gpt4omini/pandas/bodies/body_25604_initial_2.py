import pandas as pd # pragma: no cover

data = pd.Series([1, 2, None, 4]) # pragma: no cover
pd = type('Mock', (object,), {'Series': pd.Series}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/util/_doctools.py
from l3.Runtime import _l_
"""
        Convert each input to appropriate for table outplot.
        """
if isinstance(data, pd.Series):
    _l_(10234)

    if data.name is None:
        _l_(10233)

        data = data.to_frame(name="")
        _l_(10231)
    else:
        data = data.to_frame()
        _l_(10232)
data = data.fillna("NaN")
_l_(10235)
aux = data
_l_(10236)
exit(aux)
