# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Try to format axes if they are datelike.
        """
if not self.obj.index.is_unique and self.orient in ("index", "columns"):
    raise ValueError(
        f"DataFrame index must be unique for orient='{self.orient}'."
    )
if not self.obj.columns.is_unique and self.orient in (
    "index",
    "columns",
    "records",
):
    raise ValueError(
        f"DataFrame columns must be unique for orient='{self.orient}'."
    )
