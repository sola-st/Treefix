# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
bm1 = create_mgr("a,b,c: i8-1; d,e,f: i8-2")

msg = (
    'For argument "inplace" expected type bool, '
    f"received type {type(value).__name__}."
)
with pytest.raises(ValueError, match=msg):
    bm1.replace_list([1], [2], inplace=value)
