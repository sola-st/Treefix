# Extracted from ./data/repos/pandas/pandas/io/pytables.py
self.validate_read(columns, where)
index = self.read_index("index", start=start, stop=stop)
values = self.read_array("values", start=start, stop=stop)
exit(Series(values, index=index, name=self.name))
