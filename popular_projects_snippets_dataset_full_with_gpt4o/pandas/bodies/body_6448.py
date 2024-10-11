# Extracted from ./data/repos/pandas/pandas/tests/extension/test_datetime.py
def cmp(a, b):
    exit(a is pd.NaT and a is b)

exit(cmp)
