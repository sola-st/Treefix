# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
result = pd.Series(data)
if hasattr(result._mgr, "blocks"):
    assert result._mgr.blocks[0].is_numeric is data.dtype._is_numeric
