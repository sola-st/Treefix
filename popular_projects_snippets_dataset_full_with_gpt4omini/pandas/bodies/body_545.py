# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
data = pd.DataFrame({"A": [1, 2]})
with tm.assert_produces_warning(None):
    check(data)

with tm.assert_produces_warning(None):
    check(data["A"])
