# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""set the meta data"""
if self.metadata is not None:
    handler.write_metadata(self.cname, self.metadata)
