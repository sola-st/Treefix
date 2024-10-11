# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py
op = tm.get_op_from_name(all_arithmetic_operators)
s = pd.Series(data)
other = 0.01

result = op(s, other)
expected = op(s.astype(float), other)
expected = expected.astype("Float64")

# rmod results in NaN that wasn't NA in original nullable Series -> unmask it
if all_arithmetic_operators == "__rmod__":
    mask = (s == 0).fillna(False).to_numpy(bool)
    expected.array._mask[mask] = False

tm.assert_series_equal(result, expected)
