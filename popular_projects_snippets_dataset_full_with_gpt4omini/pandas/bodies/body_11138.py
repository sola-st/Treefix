# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
tups = [tuple(row) for row in df[keys].values]
tups = com.asarray_tuplesafe(tups)
expected = f(df.groupby(tups)[field])
for k, v in expected.items():
    assert result[k] == v
