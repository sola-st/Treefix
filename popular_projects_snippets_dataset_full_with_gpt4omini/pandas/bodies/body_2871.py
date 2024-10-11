# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
with pytest.raises(ValueError, match="ffil"):
    float_frame.fillna(method="ffil")
