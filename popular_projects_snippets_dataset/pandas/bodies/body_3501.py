# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# scalar qs

# result should be invariant to shuffling
indexer = np.arange(len(index), dtype=np.intp)
np.random.shuffle(indexer)
obj = obj.iloc[indexer]

qs = 0.5
result = self.compute_quantile(obj, qs)

if np_version_under1p21 and index.dtype == "timedelta64[ns]":
    msg = "failed on Numpy 1.20.3; TypeError: data type 'Int64' not understood"
    mark = pytest.mark.xfail(reason=msg, raises=TypeError)
    request.node.add_marker(mark)

exp_dtype = index.dtype
if index.dtype == "Int64":
    exp_dtype = "Float64"

expected = Series({"A": index[4]}, dtype=exp_dtype, name=0.5)
if isinstance(obj, Series):
    expected = expected["A"]
    assert result == expected
else:
    tm.assert_series_equal(result, expected)
