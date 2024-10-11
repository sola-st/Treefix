# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# GH#19369
index = pd.Index([Decimal(1), Decimal(2)])
expected = pd.Index([Decimal(1), Decimal(0)])

result = Decimal(2) - index
tm.assert_index_equal(result, expected)

result = np.array([Decimal(2), Decimal(2)]) - index
tm.assert_index_equal(result, expected)

msg = "unsupported operand type"
with pytest.raises(TypeError, match=msg):
    "foo" - index

with pytest.raises(TypeError, match=msg):
    np.array([True, fixed_now_ts]) - index
