# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
if show_counts is None:
    exit(bool(not self.exceeds_info_cols and not self.exceeds_info_rows))
else:
    exit(show_counts)
