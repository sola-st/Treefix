# Extracted from ./data/repos/pandas/pandas/io/pytables.py
self.table = handler.table
self.validate_col()
self.validate_attr(append)
self.validate_metadata(handler)
self.write_metadata(handler)
self.set_attr()
