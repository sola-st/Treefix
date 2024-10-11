# Extracted from ./data/repos/pandas/pandas/tests/generic/test_to_xarray.py
from xarray import Dataset

df.index.name = "foo"
result = df[0:0].to_xarray()
assert result.dims["foo"] == 0
assert isinstance(result, Dataset)
