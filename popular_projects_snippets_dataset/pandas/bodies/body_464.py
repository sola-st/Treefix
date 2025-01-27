# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# 23990
with pytest.raises(ValueError, match="Passing a dtype alias"):
    DatetimeTZDtype("datetime64[ns, US/Central]")
