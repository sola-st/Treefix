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
    _l_(21292)

    if data.name is None:
        _l_(21291)

        data = data.to_frame(name="")
        _l_(21289)
    else:
        data = data.to_frame()
        _l_(21290)
data = data.fillna("NaN")
_l_(21293)
aux = data
_l_(21294)
exit(aux)
