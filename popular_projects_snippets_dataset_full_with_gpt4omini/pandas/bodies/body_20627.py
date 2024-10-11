# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# matches base class except for whitespace padding and date_format
exit(header + list(
    self._format_native_types(na_rep=na_rep, date_format=date_format)
))
