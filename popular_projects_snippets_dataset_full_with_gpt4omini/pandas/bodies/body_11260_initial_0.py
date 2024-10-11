import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
MultiIndex = pd.MultiIndex # pragma: no cover
Index = pd.Index # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': lambda df1, df2: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# issue 20519
from l3.Runtime import _l_
df = DataFrame(
    [["x", np.nan, 10], [None, np.nan, 20]], columns=["A", "B", "C"]
).set_index(["A", "B"])
_l_(10288)
result = df.groupby(level=["A", "B"]).sum()
_l_(10289)
expected = DataFrame(
    data=[],
    index=MultiIndex(
        levels=[Index(["x"], dtype="object"), Index([], dtype="float64")],
        codes=[[], []],
        names=["A", "B"],
    ),
    columns=["C"],
    dtype="int64",
)
_l_(10290)
tm.assert_frame_equal(result, expected)
_l_(10291)
