# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
super().test_slice_key(obj, key, expected, val, indexer_sli, is_inplace)

if type(val) is float:
    # the xfail would xpass bc test_slice_key short-circuits
    raise AssertionError("xfail not relevant for this test.")
