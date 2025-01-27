# Extracted from ./data/repos/pandas/pandas/tests/generic/test_to_xarray.py
index = index_flat
# MultiIndex is tested in test_to_xarray_with_multiindex
if len(index) == 0:
    pytest.skip("Test doesn't make sense for empty index")

from xarray import Dataset

df.index = index[:3]
df.index.name = "foo"
df.columns.name = "bar"
result = df.to_xarray()
assert result.dims["foo"] == 3
assert len(result.coords) == 1
assert len(result.data_vars) == 8
tm.assert_almost_equal(list(result.coords.keys()), ["foo"])
assert isinstance(result, Dataset)

# idempotency
# datetimes w/tz are preserved
# column names are lost
expected = df.copy()
expected["f"] = expected["f"].astype(object)
expected.columns.name = None
tm.assert_frame_equal(result.to_dataframe(), expected)
