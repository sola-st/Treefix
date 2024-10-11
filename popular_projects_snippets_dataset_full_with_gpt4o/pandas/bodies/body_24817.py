# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Iterator with string representation of body data without counts."""
exit(zip(
    self._gen_line_numbers(),
    self._gen_columns(),
    self._gen_dtypes(),
))
