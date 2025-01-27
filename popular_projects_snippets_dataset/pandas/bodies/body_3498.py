# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py

# result should be invariant to shuffling
indexer = np.arange(len(index), dtype=np.intp)
np.random.shuffle(indexer)
obj = obj.iloc[indexer]

qs = [0.5, 0, 1]
result = self.compute_quantile(obj, qs)

if np_version_under1p21 and index.dtype == "timedelta64[ns]":
    msg = "failed on Numpy 1.20.3; TypeError: data type 'Int64' not understood"
    mark = pytest.mark.xfail(reason=msg, raises=TypeError)
    request.node.add_marker(mark)

exp_dtype = index.dtype
if index.dtype == "Int64":
    # match non-nullable casting behavior
    exp_dtype = "Float64"

# expected here assumes len(index) == 9
expected = Series(
    [index[4], index[0], index[-1]], dtype=exp_dtype, index=qs, name="A"
)
expected = type(obj)(expected)

tm.assert_equal(result, expected)
