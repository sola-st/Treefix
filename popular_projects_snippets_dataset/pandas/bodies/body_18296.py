# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# GH#19369
index = pd.Index([Decimal(1), Decimal(2)])
expected = pd.Index([Decimal(0), Decimal(1)])

result = index - Decimal(1)
tm.assert_index_equal(result, expected)

result = index - pd.Index([Decimal(1), Decimal(1)])
tm.assert_index_equal(result, expected)

msg = "unsupported operand type"
with pytest.raises(TypeError, match=msg):
    index - "foo"

with pytest.raises(TypeError, match=msg):
    index - np.array([2, "foo"], dtype=object)
