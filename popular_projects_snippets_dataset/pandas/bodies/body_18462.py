# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#13844
a = Series(dtype="M8[ns]")
b = Series(dtype="m8[ns]")
a = box_with_array(a)
b = box_with_array(b)
tm.assert_equal(a, a + b)
tm.assert_equal(a, a - b)
tm.assert_equal(a, b + a)
msg = "cannot subtract"
with pytest.raises(TypeError, match=msg):
    b - a
