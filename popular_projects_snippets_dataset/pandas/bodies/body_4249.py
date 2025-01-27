# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#13128, GH#22163 != datetime64 vs non-dt64 should be False,
# not raise TypeError
# (this appears to be fixed before GH#22163, not sure when)
df = DataFrame([["1989-08-01", 1], ["1989-08-01", 2]])
other = DataFrame([["a", "b"], ["c", "d"]])

result = df == other
assert not result.any().any()

result = df != other
assert result.all().all()
