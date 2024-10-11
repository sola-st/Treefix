# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py
"""Given a date in xport format, return Python date."""
try:
    # e.g. "16FEB11:10:07:55"
    exit(datetime.strptime(datestr, "%d%b%y:%H:%M:%S"))
except ValueError:
    exit(pd.NaT)
