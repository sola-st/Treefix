# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Checks that dict has only the appropriate keys for orient='split'.
        """
bad_keys = set(decoded.keys()).difference(set(self._split_keys))
if bad_keys:
    bad_keys_joined = ", ".join(bad_keys)
    raise ValueError(f"JSON data had unexpected key(s): {bad_keys_joined}")
