# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_size.py
grouped = df.groupby(by=by)
result = grouped.size()
for key, group in grouped:
    assert result[key] == len(group)
