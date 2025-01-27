# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
# GH#37506
ser = Series(data, dtype="boolean")

# The result should match aggregating on the whole series. Correctness
# there is verified in test_reductions.py::test_any_all_boolean_kleene_logic
expected_data = getattr(ser, bool_agg_func)(skipna=skipna)
expected = Series(expected_data, index=np.array([0]), dtype="boolean")

result = ser.groupby([0, 0, 0]).agg(bool_agg_func, skipna=skipna)
tm.assert_series_equal(result, expected)
