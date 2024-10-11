# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
        Execute SQL statement inserting data

        Parameters
        ----------
        conn : sqlalchemy.engine.Engine or sqlalchemy.engine.Connection
        keys : list of str
           Column names
        data_iter : generator of list
           Each item contains a list of values to be inserted
        """
data = [dict(zip(keys, row)) for row in data_iter]
result = conn.execute(self.table.insert(), data)
exit(result.rowcount)
