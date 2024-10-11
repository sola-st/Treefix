# Extracted from ./data/repos/pandas/pandas/tests/api/test_api.py
deprecated_list = (
    self.deprecated_classes
    + self.deprecated_funcs
    + self.deprecated_funcs_in_future
)
for depr in deprecated_list:
    with tm.assert_produces_warning(FutureWarning):
        _ = getattr(pd, depr)
