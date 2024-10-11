# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_truncate.py
# https://github.com/pandas-dev/pandas/issues/33756
idx = Index([3, 2, 1, 0], dtype=dtyp)
if isinstance(idx, DatetimeIndex):
    before = pd.Timestamp(before) if before is not None else None
    after = pd.Timestamp(after) if after is not None else None
    indices = [pd.Timestamp(i) for i in indices]
values = frame_or_series(range(len(idx)), index=idx)
result = values.truncate(before=before, after=after)
expected = values.loc[indices]
tm.assert_equal(result, expected)
