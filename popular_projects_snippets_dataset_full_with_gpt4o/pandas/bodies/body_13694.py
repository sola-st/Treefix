# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_exceptions.py
msg = "`other` must be of type `Styler`"
with pytest.raises(TypeError, match=msg):
    styler.concat(DataFrame([[1, 2]]))
