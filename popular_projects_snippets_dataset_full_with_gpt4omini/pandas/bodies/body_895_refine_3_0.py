import pandas as pd # pragma: no cover
from pandas import IndexSlice as indexer_sli # pragma: no cover
import pandas.testing as tm # pragma: no cover

frame_or_series = pd.Series # pragma: no cover
indexer_sli = lambda obj: obj.loc # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

frame_or_series = pd.Series # pragma: no cover
indexer_sli = lambda obj: obj.iloc # pragma: no cover
tm.assert_equal = staticmethod(lambda a, b: a.equals(b)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_na_indexing.py
# https://github.com/pandas-dev/pandas/issues/31503
from l3.Runtime import _l_
obj = frame_or_series([1, 2, 3])
_l_(4463)

mask = pd.array([True, False, None], dtype="boolean")
_l_(4464)

result = indexer_sli(obj)[mask]
_l_(4465)
expected = indexer_sli(obj)[mask.fillna(False)]
_l_(4466)

tm.assert_equal(result, expected)
_l_(4467)
