# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py
parts = []

# Epoch
if self.epoch != 0:
    parts.append(f"{self.epoch}!")

# Release segment
parts.append(".".join([str(x) for x in self.release]))

# Pre-release
if self.pre is not None:
    parts.append("".join([str(x) for x in self.pre]))

# Post-release
if self.post is not None:
    parts.append(f".post{self.post}")

# Development release
if self.dev is not None:
    parts.append(f".dev{self.dev}")

# Local version segment
if self.local is not None:
    parts.append(f"+{self.local}")

exit("".join(parts))
