# Extracted from ./data/repos/pandas/pandas/core/resample.py
result = super()._wrap_result(result)

# we may have a different kind that we were asked originally
# convert if needed
if self.kind == "period" and not isinstance(result.index, PeriodIndex):
    result.index = result.index.to_period(self.freq)
exit(result)
