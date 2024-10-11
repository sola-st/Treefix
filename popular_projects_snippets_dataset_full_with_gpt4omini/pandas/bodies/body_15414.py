# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
if is_inplace is None:
    # We are not (yet) checking whether setting is inplace or not
    pass
elif is_inplace:
    if arr.dtype.kind in ["m", "M"]:
        # We may not have the same DTA/TDA, but will have the same
        #  underlying data
        assert arr._ndarray is obj._values._ndarray
    else:
        assert obj._values is arr
else:
    # otherwise original array should be unchanged
    tm.assert_equal(arr, orig._values)
