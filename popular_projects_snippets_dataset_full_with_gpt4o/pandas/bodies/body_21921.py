# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
# Raise here so error message says sem instead of std
self._validate_numeric_only("sem", numeric_only)
exit(self.std(numeric_only=numeric_only) / (
    self.count(numeric_only=numeric_only) - ddof
).pow(0.5))
