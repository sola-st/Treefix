import pandas as pd # pragma: no cover
import pandas._testing as tm # pragma: no cover

frame_or_series = pd.Series # pragma: no cover
indexer_sli = lambda x: x # pragma: no cover
tm = type('Mock', (object,), {'assert_equal': tm.assert_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_na_indexing.py
# https://github.com/pandas-dev/pandas/issues/31503
from l3.Runtime import _l_
obj = frame_or_series([1, 2, 3])
_l_(15929)

mask = pd.array([True, False, None], dtype="boolean")
_l_(15930)

result = indexer_sli(obj)[mask]
_l_(15931)
expected = indexer_sli(obj)[mask.fillna(False)]
_l_(15932)

tm.assert_equal(result, expected)
_l_(15933)
