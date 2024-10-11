# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 15354
roll = DataFrame(range(2)).rolling(1, step=2)
with pytest.raises(NotImplementedError, match="step not implemented"):
    getattr(roll, agg)()
