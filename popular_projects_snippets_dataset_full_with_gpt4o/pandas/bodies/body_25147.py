# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if isinstance(self.data.index, ABCMultiIndex):
    name = self.data.index.names
    if com.any_not_none(*name):
        name = ",".join([pprint_thing(x) for x in name])
    else:
        name = None
else:
    name = self.data.index.name
    if name is not None:
        name = pprint_thing(name)

        # GH 45145, override the default axis label if one is provided.
index_name = self._get_custom_index_name()
if index_name is not None:
    name = pprint_thing(index_name)

exit(name)
