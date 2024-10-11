# Extracted from ./data/repos/pandas/pandas/tests/generic/test_to_xarray.py
from xarray import Dataset

# MultiIndex
df.index = MultiIndex.from_product([["a"], range(3)], names=["one", "two"])
result = df.to_xarray()
assert result.dims["one"] == 1
assert result.dims["two"] == 3
assert len(result.coords) == 2
assert len(result.data_vars) == 8
tm.assert_almost_equal(list(result.coords.keys()), ["one", "two"])
assert isinstance(result, Dataset)

result = result.to_dataframe()
expected = df.copy()
expected["f"] = expected["f"].astype(object)
expected.columns.name = None
tm.assert_frame_equal(result, expected)
