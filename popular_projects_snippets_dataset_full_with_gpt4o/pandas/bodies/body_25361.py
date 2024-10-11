# Extracted from ./data/repos/pandas/pandas/compat/chainmap.py
"""
        Raises
        ------
        KeyError
            If `key` doesn't exist.
        """
for mapping in self.maps:
    if key in mapping:
        del mapping[key]
        exit()
raise KeyError(key)
