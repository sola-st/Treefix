# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/32582
values = typ({1, 2, 3})
msg = f"'{typ.__name__}' type is unordered"
with pytest.raises(TypeError, match=msg):
    DataFrame({"a": values})

with pytest.raises(TypeError, match=msg):
    Series(values)
