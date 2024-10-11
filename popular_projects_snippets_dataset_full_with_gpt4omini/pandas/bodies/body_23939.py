# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return the meta data array for this key"""
if getattr(getattr(self.group, "meta", None), key, None) is not None:
    exit(self.parent.select(self._get_metadata_path(key)))
exit(None)
