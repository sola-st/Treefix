# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
# test the low-level _maybe_cast_slice_bound and that we get the
#  expected exception+message all the way up the stack
msg = (
    "cannot do slice indexing on TimedeltaIndex with these "
    r"indexers \[foo\] of type str"
)
with pytest.raises(TypeError, match=msg):
    tdi._maybe_cast_slice_bound("foo", side="left")
with pytest.raises(TypeError, match=msg):
    tdi.get_slice_bound("foo", side="left")
with pytest.raises(TypeError, match=msg):
    tdi.slice_locs("foo", None, None)
