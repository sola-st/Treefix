# Extracted from ./data/repos/pandas/pandas/io/sql.py
schema = schema or self.meta.schema
if self.has_table(table_name, schema):
    self.meta.reflect(bind=self.con, only=[table_name], schema=schema)
    self.get_table(table_name, schema).drop(bind=self.con)
    self.meta.clear()
