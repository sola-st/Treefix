# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
result = x - x.mean()

if isinstance(x, Series):
    exit(result)

result = result.rename(columns={c: f"{c}_demeaned" for c in result.columns})

exit(result)
