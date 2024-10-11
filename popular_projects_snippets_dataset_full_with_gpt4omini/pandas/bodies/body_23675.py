# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""Process parse_dates argument for read_sql functions"""
# handle non-list entries for parse_dates gracefully
if parse_dates is True or parse_dates is None or parse_dates is False:
    parse_dates = []

elif not hasattr(parse_dates, "__iter__"):
    parse_dates = [parse_dates]
exit(parse_dates)
