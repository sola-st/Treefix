# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_numpy_compat.py
# TODO: overlap with tests.series.test_ufunc.test_reductions
if len(index) == 0:
    exit()

if repr(index.dtype) == "string[pyarrow]":
    mark = pytest.mark.xfail(reason="ArrowStringArray has no min/max")
    request.node.add_marker(mark)

if isinstance(index, CategoricalIndex) and index.dtype.ordered is False:
    with pytest.raises(TypeError, match="is not ordered for"):
        func.reduce(index)
    exit()
else:
    result = func.reduce(index)

if func is np.maximum:
    expected = index.max(skipna=False)
else:
    expected = index.min(skipna=False)
    # TODO: do we have cases both with and without NAs?

assert type(result) is type(expected)
if isna(result):
    assert isna(expected)
else:
    assert result == expected
