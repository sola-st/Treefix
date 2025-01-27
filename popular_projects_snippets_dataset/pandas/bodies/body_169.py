# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# datetime/timedelta
df = DataFrame(np.random.random((3, 4)))
df[col] = val
result = df.applymap(str)
assert result.loc[0, col] == str(df.loc[0, col])
