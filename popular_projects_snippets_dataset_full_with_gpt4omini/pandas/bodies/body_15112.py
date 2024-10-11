# Extracted from ./data/repos/pandas/pandas/tests/base/test_value_counts.py
klass = index_or_series

# GH 3002, datetime64[ns]
# don't test names though
df = pd.DataFrame(
    {
        "person_id": ["xxyyzz", "xxyyzz", "xxyyzz", "xxyyww", "foofoo", "foofoo"],
        "dt": pd.to_datetime(
            [
                "2010-01-01",
                "2010-01-01",
                "2010-01-01",
                "2009-01-01",
                "2008-09-09",
                "2008-09-09",
            ]
        ),
        "food": ["PIE", "GUM", "EGG", "EGG", "PIE", "GUM"],
    }
)

s = klass(df["dt"].copy())
s.name = None
idx = pd.to_datetime(
    ["2010-01-01 00:00:00", "2008-09-09 00:00:00", "2009-01-01 00:00:00"]
)
expected_s = Series([3, 2, 1], index=idx)
tm.assert_series_equal(s.value_counts(), expected_s)

expected = pd.array(
    np.array(
        ["2010-01-01 00:00:00", "2009-01-01 00:00:00", "2008-09-09 00:00:00"],
        dtype="datetime64[ns]",
    )
)
if isinstance(s, Index):
    tm.assert_index_equal(s.unique(), DatetimeIndex(expected))
else:
    tm.assert_extension_array_equal(s.unique(), expected)

assert s.nunique() == 3

# with NaT
s = df["dt"].copy()
s = klass(list(s.values) + [pd.NaT] * 4)

result = s.value_counts()
assert result.index.dtype == "datetime64[ns]"
tm.assert_series_equal(result, expected_s)

result = s.value_counts(dropna=False)
expected_s = pd.concat([Series([4], index=DatetimeIndex([pd.NaT])), expected_s])
tm.assert_series_equal(result, expected_s)

assert s.dtype == "datetime64[ns]"
unique = s.unique()
assert unique.dtype == "datetime64[ns]"

# numpy_array_equal cannot compare pd.NaT
if isinstance(s, Index):
    exp_idx = DatetimeIndex(expected.tolist() + [pd.NaT])
    tm.assert_index_equal(unique, exp_idx)
else:
    tm.assert_extension_array_equal(unique[:3], expected)
    assert pd.isna(unique[3])

assert s.nunique() == 3
assert s.nunique(dropna=False) == 4

# timedelta64[ns]
td = df.dt - df.dt + timedelta(1)
td = klass(td, name="dt")

result = td.value_counts()
expected_s = Series([6], index=[Timedelta("1day")], name="dt")
tm.assert_series_equal(result, expected_s)

expected = TimedeltaIndex(["1 days"], name="dt")
if isinstance(td, Index):
    tm.assert_index_equal(td.unique(), expected)
else:
    tm.assert_extension_array_equal(td.unique(), expected._values)

td2 = timedelta(1) + (df.dt - df.dt)
td2 = klass(td2, name="dt")
result2 = td2.value_counts()
tm.assert_series_equal(result2, expected_s)
