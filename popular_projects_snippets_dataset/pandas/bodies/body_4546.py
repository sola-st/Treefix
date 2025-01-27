# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
if isinstance(obj, Series):
    exit(obj.iloc[0])
else:
    exit(obj.iloc[0, 0])
