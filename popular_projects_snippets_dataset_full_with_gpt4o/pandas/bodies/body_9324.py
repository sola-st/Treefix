# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_arrow_compat.py
if pa.types.is_boolean(arrow_type):
    exit(pd.BooleanDtype())
elif pa.types.is_integer(arrow_type):
    exit(pd.Int64Dtype())
