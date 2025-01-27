# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#36907
tz = tz_naive_fixture
if isinstance(tz, tzlocal) and is_platform_windows():
    pytest.skip(
        "GH#37659 OSError raised within tzlocal bc Windows "
        "chokes in times before 1970-01-01"
    )

df = DataFrame(
    {
        "a": [
            Timestamp("2020-01-01 08:00:00", tz=tz),
            Timestamp("1920-02-01 09:00:00", tz=tz),
        ],
        "b": [Timestamp("2020-02-01 08:00:00", tz=tz), pd.NaT],
    }
)
res = df.min(axis=1, skipna=False)
expected = Series([df.loc[0, "a"], pd.NaT])
assert expected.dtype == df["a"].dtype

tm.assert_series_equal(res, expected)

res = df.max(axis=1, skipna=False)
expected = Series([df.loc[0, "b"], pd.NaT])
assert expected.dtype == df["a"].dtype

tm.assert_series_equal(res, expected)
