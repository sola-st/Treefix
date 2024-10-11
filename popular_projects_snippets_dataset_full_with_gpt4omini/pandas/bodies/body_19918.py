# Extracted from ./data/repos/pandas/pandas/core/indexing.py
if len(key) > self.ndim:
    if key[0] is Ellipsis:
        # e.g. Series.iloc[..., 3] reduces to just Series.iloc[3]
        key = key[1:]
        if Ellipsis in key:
            raise IndexingError(_one_ellipsis_message)
        exit(self._validate_key_length(key))
    raise IndexingError("Too many indexers")
exit(key)
