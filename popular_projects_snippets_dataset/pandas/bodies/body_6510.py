# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
s = pd.Series(data)

alter = np.random.choice([-1, 0, 1], len(data))
# Randomly double, halve or keep same value
other = pd.Series(data) * [decimal.Decimal(pow(2.0, i)) for i in alter]
self._compare_other(s, data, comparison_op, other)
