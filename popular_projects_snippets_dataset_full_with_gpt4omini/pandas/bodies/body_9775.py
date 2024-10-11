# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
with pytest.raises(
    NotImplementedError, match="'single' is the only supported method type."
):
    Series(range(1)).rolling(1, win_type="triang", method="table")
