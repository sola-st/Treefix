# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
msg = "``data`` must be a Series or DataFrame"
with pytest.raises(TypeError, match=msg):
    Styler([1, 2, 3])
