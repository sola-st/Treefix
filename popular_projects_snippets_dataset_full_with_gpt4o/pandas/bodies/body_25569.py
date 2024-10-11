# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
if reason is None:
    reason = f"NumPy {ver_str} or greater required"
exit(pytest.mark.skipif(
    Version(np.__version__) < Version(ver_str),
    *args,
    reason=reason,
))
