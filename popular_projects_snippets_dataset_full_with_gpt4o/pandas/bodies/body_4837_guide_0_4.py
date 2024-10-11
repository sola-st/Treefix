import numpy as np # pragma: no cover
from pandas import Index, MultiIndex # pragma: no cover
import pytest # pragma: no cover
from pandas import testing as tm # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
from l3.Runtime import _l_
idx = Index(["some_unequal_splits", "one_of_these_things_is_not", np.nan, None])
_l_(22098)
result = idx.str.split("_", expand=True)
_l_(22099)
exp = MultiIndex.from_tuples(
    [
        ("some", "unequal", "splits", np.nan, np.nan, np.nan),
        ("one", "of", "these", "things", "is", "not"),
        (np.nan, np.nan, np.nan, np.nan, np.nan, np.nan),
        (None, None, None, None, None, None),
    ]
)
_l_(22100)
tm.assert_index_equal(result, exp)
_l_(22101)
assert result.nlevels == 6
_l_(22102)

with pytest.raises(ValueError, match="expand must be"):
    _l_(22104)

    idx.str.split("_", expand="not_a_boolean")
    _l_(22103)
