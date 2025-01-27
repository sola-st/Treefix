# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
op = getattr(operator, op)
data1 = np.random.randn(20)
data2 = np.random.randn(20)

data1[::2] = fill_value
data2[::3] = fill_value

first = SparseArray(data1, fill_value=fill_value)
second = SparseArray(data2, fill_value=fill_value)

with np.errstate(all="ignore"):
    res = op(first, second)
    exp = SparseArray(
        op(first.to_dense(), second.to_dense()), fill_value=first.fill_value
    )
    assert isinstance(res, SparseArray)
    tm.assert_almost_equal(res.to_dense(), exp.to_dense())

    res2 = op(first, second.to_dense())
    assert isinstance(res2, SparseArray)
    tm.assert_sp_array_equal(res, res2)

    res3 = op(first.to_dense(), second)
    assert isinstance(res3, SparseArray)
    tm.assert_sp_array_equal(res, res3)

    res4 = op(first, 4)
    assert isinstance(res4, SparseArray)

    # Ignore this if the actual op raises (e.g. pow).
    try:
        exp = op(first.to_dense(), 4)
        exp_fv = op(first.fill_value, 4)
    except ValueError:
        pass
    else:
        tm.assert_almost_equal(res4.fill_value, exp_fv)
        tm.assert_almost_equal(res4.to_dense(), exp)
