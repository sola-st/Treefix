# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_invalid.py
df1 = tm.makeCustomDataframe(10, 2)
msg = (
    "first argument must be an iterable of pandas "
    'objects, you passed an object of type "DataFrame"'
)
with pytest.raises(TypeError, match=msg):
    concat(df1)
