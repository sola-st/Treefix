# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
result = float_frame * 2
tm.assert_numpy_array_equal(result.values, float_frame.values * 2)

# vs mix
result = mixed_float_frame * 2
for c, s in result.items():
    tm.assert_numpy_array_equal(s.values, mixed_float_frame[c].values * 2)
_check_mixed_float(result, dtype={"C": None})

result = DataFrame() * 2
assert result.index.equals(DataFrame().index)
assert len(result.columns) == 0
