# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# look at all the amazing combinations!
month_prefixes = ["A", "AS", "BA", "BAS", "Q", "BQ", "BQS", "QS"]
names = [
    prefix + "-" + month
    for prefix in month_prefixes
    for month in [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
    ]
]
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
names += ["W-" + day for day in days]
names += ["WOM-" + week + day for week in ("1", "2", "3", "4") for day in days]
_offset_map.clear()
for name in names:
    offset = _get_offset(name)
    assert offset.freqstr == name
