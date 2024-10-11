# Extracted from ./data/repos/pandas/pandas/tests/extension/test_period.py
# we don't implement + for Period
s = pd.Series(data)
msg = (
    r"unsupported operand type\(s\) for \+: "
    r"\'PeriodArray\' and \'PeriodArray\'"
)
with pytest.raises(TypeError, match=msg):
    s + data
