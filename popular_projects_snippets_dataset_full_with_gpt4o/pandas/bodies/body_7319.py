# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
rng = timedelta_range("1 days, 10:11:12", periods=2, freq="s")
rng.components

# with nat
s = Series(rng)
s[1] = np.nan

result = s.dt.components
assert not result.iloc[0].isna().all()
assert result.iloc[1].isna().all()
