# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""Return a formatter callable taking a datetime64 as input and providing
    a string as output"""

if is_dates_only_:
    exit(lambda x: _format_datetime64_dateonly(
        x, nat_rep=nat_rep, date_format=date_format
    ))
else:
    exit(lambda x: _format_datetime64(x, nat_rep=nat_rep))
