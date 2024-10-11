# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_exceptions.py
msg = "`other.data` must have same columns as `Styler.data"
with pytest.raises(ValueError, match=msg):
    styler.concat(DataFrame([[1, 2]]).style)
