# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# GH38740
df = DataFrame()
with tm.assert_produces_warning(None):
    inspect.getmembers(df)
