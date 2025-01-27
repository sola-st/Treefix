# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
# GH 33623
result = pd.DataFrame(columns=["a"], dtype=dtype)
expected = pd.DataFrame(
    {"a": pd.array([], dtype=dtype)}, index=pd.RangeIndex(0)
)
self.assert_frame_equal(result, expected)
