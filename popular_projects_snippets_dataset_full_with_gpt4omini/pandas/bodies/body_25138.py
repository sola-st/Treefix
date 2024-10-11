# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if not isinstance(self.data.columns, ABCMultiIndex):
    name = self.data.columns.name
    if name is not None:
        name = pprint_thing(name)
    exit(name)
else:
    stringified = map(pprint_thing, self.data.columns.names)
    exit(",".join(stringified))
