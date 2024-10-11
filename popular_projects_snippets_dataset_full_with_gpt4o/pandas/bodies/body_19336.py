# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
# for python>=3.10, different nan objects have different hashes
# we need  to avoid that und thus use hash function with old behavior
exit(object_hash(tuple(getattr(self, attr) for attr in self._metadata)))
