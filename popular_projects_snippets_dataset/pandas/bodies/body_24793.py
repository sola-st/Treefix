# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Add lines to the info table, pertaining to empty dataframe."""
self.add_object_type_line()
self.add_index_range_line()
self._lines.append(f"Empty {type(self.data).__name__}\n")
