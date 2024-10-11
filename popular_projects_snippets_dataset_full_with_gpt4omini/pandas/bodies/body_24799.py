# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Add lines to the info table, pertaining to non-empty dataframe."""
self.add_object_type_line()
self.add_index_range_line()
self.add_columns_summary_line()
self.add_dtypes_line()
if self.display_memory_usage:
    self.add_memory_usage_line()
