# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_level_values.py
# GH33131. See also discussion in GH32669.
# This test can probably be removed when PeriodIndex._engine is removed.
from pandas import (
    Period,
    PeriodIndex,
)

idx = MultiIndex.from_arrays(
    [PeriodIndex([Period("2019Q1"), Period("2019Q2")], name="b")]
)
idx2 = MultiIndex.from_arrays(
    [idx._get_level_values(level) for level in range(idx.nlevels)]
)
assert all(x.is_monotonic_increasing for x in idx2.levels)
