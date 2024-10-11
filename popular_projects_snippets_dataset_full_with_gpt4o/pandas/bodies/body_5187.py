# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
msg = "Invalid type <class 'str'>. Must be int or float."
with pytest.raises(TypeError, match=msg):
    Timedelta(nanoseconds="abc")
