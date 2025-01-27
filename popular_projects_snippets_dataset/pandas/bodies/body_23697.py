# Extracted from ./data/repos/pandas/pandas/io/sql.py
# Inserting table into database, add to MetaData object
self.table = self.table.to_metadata(self.pd_sql.meta)
self.table.create(bind=self.pd_sql.con)
