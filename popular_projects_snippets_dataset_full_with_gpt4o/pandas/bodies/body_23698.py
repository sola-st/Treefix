# Extracted from ./data/repos/pandas/pandas/io/sql.py
if self.exists():
    if self.if_exists == "fail":
        raise ValueError(f"Table '{self.name}' already exists.")
    if self.if_exists == "replace":
        self.pd_sql.drop_table(self.name, self.schema)
        self._execute_create()
    elif self.if_exists == "append":
        pass
    else:
        raise ValueError(f"'{self.if_exists}' is not valid for if_exists")
else:
    self._execute_create()
