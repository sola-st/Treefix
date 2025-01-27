# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# bad input
msg = "invalid how option: foo"
with pytest.raises(ValueError, match=msg):
    float_frame.dropna(how="foo")
# non-existent column - 8303
with pytest.raises(KeyError, match=r"^\['X'\]$"):
    float_frame.dropna(subset=["A", "X"])
