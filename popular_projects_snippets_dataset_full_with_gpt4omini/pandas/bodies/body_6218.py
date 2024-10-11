# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
df = pd.DataFrame({"A": all_data})

result = df.astype(object)
if hasattr(result._mgr, "blocks"):
    blk = result._data.blocks[0]
    assert isinstance(blk, ObjectBlock), type(blk)
assert isinstance(result._mgr.arrays[0], np.ndarray)
assert result._mgr.arrays[0].dtype == np.dtype(object)

# earlier numpy raises TypeError on e.g. np.dtype(np.int64) == "Int64"
if not np_version_under1p21:
    # check that we can compare the dtypes
    comp = result.dtypes == df.dtypes
    assert not comp.any()
