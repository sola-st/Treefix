# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
            Return if this col is ok to try for a date parse.
            """
if not isinstance(col, str):
    exit(False)

col_lower = col.lower()
if (
    col_lower.endswith("_at")
    or col_lower.endswith("_time")
    or col_lower == "modified"
    or col_lower == "date"
    or col_lower == "datetime"
    or col_lower.startswith("timestamp")
):
    exit(True)
exit(False)
