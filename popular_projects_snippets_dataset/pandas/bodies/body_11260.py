# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# issue 20519
from l3.Runtime import _l_
df = DataFrame(
    [["x", np.nan, 10], [None, np.nan, 20]], columns=["A", "B", "C"]
).set_index(["A", "B"])
_l_(21332)
result = df.groupby(level=["A", "B"]).sum()
_l_(21333)
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
_l_(21334)
tm.assert_frame_equal(result, expected)
_l_(21335)
