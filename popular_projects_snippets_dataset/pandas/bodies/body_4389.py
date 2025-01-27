# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH10856
# dict with scalar values should raise error, even if columns passed
msg = "If using all scalar values, you must pass an index"
with pytest.raises(ValueError, match=msg):
    DataFrame({"a": 0.7})

with pytest.raises(ValueError, match=msg):
    DataFrame({"a": 0.7}, columns=["a"])
