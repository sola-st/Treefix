# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
idx = simple_index

if idx.dtype.kind in ["i", "u"]:
    res = ~idx
    expected = Index(~idx.values, name=idx.name)
    tm.assert_index_equal(res, expected)

    # check that we are matching Series behavior
    res2 = ~Series(idx)
    # TODO(2.0): once we preserve dtype, check_dtype can be True
    tm.assert_series_equal(res2, Series(expected), check_dtype=False)
else:
    if idx.dtype.kind == "f":
        msg = "ufunc 'invert' not supported for the input types"
    else:
        msg = "bad operand"
    with pytest.raises(TypeError, match=msg):
        ~idx

    # check that we get the same behavior with Series
    with pytest.raises(TypeError, match=msg):
        ~Series(idx)
