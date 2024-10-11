import re # pragma: no cover
import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from datetime import datetime # pragma: no cover
import pandas.testing as tm # pragma: no cover

Series = pd.Series # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
from l3.Runtime import _l_
pat = re.compile(r"BAD_*")
_l_(10650)
ser = Series(
    ["aBAD", np.nan, "bBAD", True, datetime.today(), "fooBAD", None, 1, 2.0]
)
_l_(10651)
result = Series(ser).str.replace(pat, "", regex=True)
_l_(10652)
expected = Series(["a", np.nan, "b", np.nan, np.nan, "foo", np.nan, np.nan, np.nan])
_l_(10653)
tm.assert_series_equal(result, expected)
_l_(10654)
