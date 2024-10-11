# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_clip.py

sers = [
    Series([np.nan, 1.0, 2.0, 3.0]),
    Series([None, "a", "b", "c"]),
    Series(pd.to_datetime([np.nan, 1, 2, 3], unit="D")),
]

for s in sers:
    thresh = s[2]
    lower = s.clip(lower=thresh)
    upper = s.clip(upper=thresh)
    assert lower[notna(lower)].min() == thresh
    assert upper[notna(upper)].max() == thresh
    assert list(isna(s)) == list(isna(lower))
    assert list(isna(s)) == list(isna(upper))
