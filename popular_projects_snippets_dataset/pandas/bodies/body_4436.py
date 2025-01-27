# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 32173
arrays = [list("abc"), list("cde")]

msg = "3 columns passed, passed data had 4"
with pytest.raises(ValueError, match=msg):
    DataFrame([[1, 2, 3, 4], [4, 5, 6, 7]], columns=arrays)
