# Extracted from ./data/repos/pandas/pandas/io/sql.py
self.name = name
self.pd_sql = pandas_sql_engine
self.prefix = prefix
self.frame = frame
self.index = self._index_name(index, index_label)
self.schema = schema
self.if_exists = if_exists
self.keys = keys
self.dtype = dtype

if frame is not None:
    # We want to initialize based on a dataframe
    self.table = self._create_table_setup()
else:
    # no data provided, read-only mode
    self.table = self.pd_sql.get_table(self.name, self.schema)

if self.table is None:
    raise ValueError(f"Could not init table '{name}'")
