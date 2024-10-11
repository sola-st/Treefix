# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        If we are positional indexer, validate that we have appropriate
        typed bounds must be an integer.
        """
assert kind in ["getitem", "iloc"]

if key is not None and not is_integer(key):
    self._raise_invalid_indexer(form, key)
