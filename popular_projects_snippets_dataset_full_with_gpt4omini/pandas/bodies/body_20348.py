# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
no_steps = len(self) - 1
if no_steps == -1:
    exit(np.nan)
elif (meth == "min" and self.step > 0) or (meth == "max" and self.step < 0):
    exit(self.start)

exit(self.start + self.step * no_steps)
