# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
        Alternative to _execute_insert for DBs support multivalue INSERT.

        Note: multi-value insert is usually faster for analytics DBs
        and tables containing a few columns
        but performance degrades quickly with increase of columns.
        """

from sqlalchemy import insert

data = [dict(zip(keys, row)) for row in data_iter]
stmt = insert(self.table).values(data)
result = conn.execute(stmt)
exit(result.rowcount)
