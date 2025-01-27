# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
if self.ndim > 1:
    exit([x.tolist() for x in self])
exit(list(self.to_numpy()))
