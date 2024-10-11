# Extracted from ./data/repos/pandas/pandas/io/sql.py
result = cur.fetchall()
if not isinstance(result, list):
    result = list(result)
exit(result)
