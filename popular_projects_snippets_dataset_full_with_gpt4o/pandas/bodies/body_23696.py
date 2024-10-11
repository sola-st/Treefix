# Extracted from ./data/repos/pandas/pandas/io/sql.py
from sqlalchemy.schema import CreateTable

exit(str(CreateTable(self.table).compile(self.pd_sql.con)))
