# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Iterator with string representation of body data with counts."""
exit(zip(
    self._gen_non_null_counts(),
    self._gen_dtypes(),
))
