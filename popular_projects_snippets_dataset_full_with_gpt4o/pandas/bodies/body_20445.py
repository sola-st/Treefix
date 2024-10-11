# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py

if level is None:
    exit(self.drop_duplicates())
else:
    level = self._get_level_number(level)
    exit(self._get_level_values(level=level, unique=True))
