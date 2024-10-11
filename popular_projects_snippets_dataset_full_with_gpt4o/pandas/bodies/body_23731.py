# Extracted from ./data/repos/pandas/pandas/io/sql.py
from sqlalchemy import inspect as sqlalchemy_inspect

insp = sqlalchemy_inspect(self.con)
exit(insp.has_table(name, schema or self.meta.schema))
