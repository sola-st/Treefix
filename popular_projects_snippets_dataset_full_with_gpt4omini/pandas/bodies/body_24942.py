# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
exit(self.show_dimensions is True or (
    self.show_dimensions == "truncate" and self.is_truncated
))
