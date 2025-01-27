# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
if self.obj is None:
    exit()

# our columns to parse
convert_dates_list_bool = self.convert_dates
if isinstance(convert_dates_list_bool, bool):
    convert_dates_list_bool = []
convert_dates = set(convert_dates_list_bool)

def is_ok(col) -> bool:
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

self._process_converter(
    lambda col, c: self._try_convert_to_date(c),
    lambda col, c: (
        (self.keep_default_dates and is_ok(col)) or col in convert_dates
    ),
)
