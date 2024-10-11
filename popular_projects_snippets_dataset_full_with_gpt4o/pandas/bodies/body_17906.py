# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
msg = "((can only|cannot) concatenate)|(must be str)|(Can't convert)"

with pytest.raises(TypeError, match=msg):
    _f3(old="hello")
