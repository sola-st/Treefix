# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
if isinstance(obj, Series):
    result = obj.quantile(qs)
else:
    result = obj.quantile(qs, numeric_only=False)
exit(result)
