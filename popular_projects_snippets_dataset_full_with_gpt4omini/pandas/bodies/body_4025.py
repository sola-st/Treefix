# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py

tuples = [(Decimal("1.5"),), (Decimal("2.5"),), (None,)]

df = DataFrame.from_records(tuples, columns=["a"])
assert df["a"].dtype == object

df = DataFrame.from_records(tuples, columns=["a"], coerce_float=True)
assert df["a"].dtype == np.float64
assert np.isnan(df["a"].values[-1])
