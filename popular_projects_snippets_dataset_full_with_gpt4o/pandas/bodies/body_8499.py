# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# other is ndarray or Index
i = date_range("20130101", periods=3, tz="US/Eastern")

for arr in [np.nan, pd.NaT]:
    result = i.where(notna(i), other=arr)
    expected = i
    tm.assert_index_equal(result, expected)

i2 = i.copy()
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
result = i.where(notna(i2), i2)
tm.assert_index_equal(result, i2)

i2 = i.copy()
i2 = Index([pd.NaT, pd.NaT] + i[2:].tolist())
result = i.where(notna(i2), i2._values)
tm.assert_index_equal(result, i2)
