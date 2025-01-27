# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 32173
arrays = [list("abcd"), list("cde")]

# exception raised inside MultiIndex constructor
msg = "all arrays must be same length"
with pytest.raises(ValueError, match=msg):
    DataFrame([[1, 2, 3, 4], [4, 5, 6, 7]], columns=arrays)
