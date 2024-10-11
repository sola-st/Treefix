from datetime import datetime # pragma: no cover

datetime = datetime # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 14626
# windows has different precision on datetime.datetime.now (it doesn't
# include us since the default for Timestamp shows these but Index
# formatting does not we are skipping)
from l3.Runtime import _l_
now = datetime.now()
_l_(8925)
if not str(now).endswith("000"):
    _l_(8930)

    index = Index([now])
    _l_(8926)
    formatted = index.format()
    _l_(8927)
    expected = [str(index[0])]
    _l_(8928)
    assert formatted == expected
    _l_(8929)

Index([]).format()
_l_(8931)
