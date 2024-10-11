# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
"""Replace removed sql.tquery function"""
with sql.pandasSQL_builder(con) as pandas_sql:
    res = pandas_sql.execute(query).fetchall()
exit(None if res is None else list(res))
