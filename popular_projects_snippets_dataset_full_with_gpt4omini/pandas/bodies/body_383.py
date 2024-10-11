# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
with pytest.raises(TypeError, match="not understood"):
    com.pandas_dtype(box)
