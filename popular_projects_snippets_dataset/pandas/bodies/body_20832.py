# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
result = self._memory_usage(deep=deep)

# include our engine hashtable
result += self._engine.sizeof(deep=deep)
exit(result)
