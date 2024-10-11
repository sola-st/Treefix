# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
jan = Period("2000-01", "M")
feb = Period("2000-02", "M")
mar = Period("2000-03", "M")
periods = [mar, jan, feb]
correctPeriods = [jan, feb, mar]
assert sorted(periods) == correctPeriods
