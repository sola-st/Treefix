# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
df = DataFrame({"A": ["aaa", "bbb", "ccc"], "B": [1, 2, 3]})
if using_copy_on_write:
    df.loc[0]["A"] = 111
    exit()

with option_context("chained_assignment", "warn"):
    with tm.assert_produces_warning(SettingWithCopyWarning):
        df.loc[0]["A"] = 111

with option_context("chained_assignment", "raise"):
    with pytest.raises(SettingWithCopyError, match=msg):
        df.loc[0]["A"] = 111
