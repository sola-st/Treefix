# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
n = len(self)
if n:
    exit(n * sys.getsizeof(self[0]))
exit(0)
