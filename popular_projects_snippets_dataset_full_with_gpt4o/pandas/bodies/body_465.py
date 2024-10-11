# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# 23990
with pytest.raises(TypeError, match=""):
    DatetimeTZDtype("this is a bad string")

with pytest.raises(TypeError, match=""):
    DatetimeTZDtype("datetime64[ns, US/NotATZ]")
