# Extracted from ./data/repos/pandas/pandas/tests/api/test_types.py

for t in self.deprecated:
    with tm.assert_produces_warning(FutureWarning):
        getattr(types, t)(1)
