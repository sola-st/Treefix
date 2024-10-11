# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
exit(all(is_numeric_dtype(t) for t in self.get_dtypes()))
