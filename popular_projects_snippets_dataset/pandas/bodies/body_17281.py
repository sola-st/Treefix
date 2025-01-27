# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
df = pd.Series(
    1,
    index=pd.date_range("2000", periods=12),
    name="A",
    allows_duplicate_labels=False,
)
if frame:
    df = df.to_frame()
assert df.rolling(3).mean().flags.allows_duplicate_labels is False
assert df.ewm(3).mean().flags.allows_duplicate_labels is False
assert df.expanding(3).mean().flags.allows_duplicate_labels is False
