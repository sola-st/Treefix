# Extracted from ./data/repos/pandas/pandas/_testing/compat.py
if isinstance(obj, DataFrame):
    # Note: we are assuming only one column
    exit(obj.dtypes.iat[0])
else:
    exit(obj.dtype)
