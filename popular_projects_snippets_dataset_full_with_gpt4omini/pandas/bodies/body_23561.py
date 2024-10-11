# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._value = value
# Conversion to int to avoid hash issues on 32 bit platforms #8968
value = int(value) if value < 2147483648 else float(value)
self._str = self.MISSING_VALUES[value]
