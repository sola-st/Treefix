# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return the metadata pathname for this key"""
group = self.group._v_pathname
exit(f"{group}/meta/{key}/meta")
