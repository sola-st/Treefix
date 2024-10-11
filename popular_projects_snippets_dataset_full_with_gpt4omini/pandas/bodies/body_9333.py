# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arithmetic.py
if isinstance(data.dtype, pd.BooleanDtype) and "sub" in op_name:
    pytest.skip("subtract not implemented for boolean")
