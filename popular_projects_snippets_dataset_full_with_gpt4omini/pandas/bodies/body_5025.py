# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
s = pd.Series(pd.array(values, dtype=dtype))
if as_frame:
    s = s.to_frame(name="A")
result = tm.round_trip_pickle(s)
tm.assert_equal(result, s)
