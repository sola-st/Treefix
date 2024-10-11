# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py
parts = []

# Epoch
if self.epoch != 0:
    parts.append(f"{self.epoch}!")

# Release segment
parts.append(".".join([str(x) for x in self.release]))

exit("".join(parts))
