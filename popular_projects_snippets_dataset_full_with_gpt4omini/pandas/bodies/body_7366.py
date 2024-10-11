# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
tdi = timedelta_range(1, periods=5)

cat = pd.Categorical(tdi)

result = TimedeltaIndex(cat)
tm.assert_index_equal(result, tdi)

ci = pd.CategoricalIndex(tdi)
result = TimedeltaIndex(ci)
tm.assert_index_equal(result, tdi)
