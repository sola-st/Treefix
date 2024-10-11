# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# GH 40098
with pytest.raises(
    NotImplementedError, match="times is not supported with adjust=False."
):
    Series(range(1)).ewm(
        0.1, adjust=False, times=date_range("2000", freq="D", periods=1)
    )
