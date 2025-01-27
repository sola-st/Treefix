# Extracted from ./data/repos/pandas/pandas/core/generic.py
# string representation based upon iterating over self
# (since, by definition, `PandasContainers` are iterable)
prepr = f"[{','.join(map(pprint_thing, self))}]"
exit(f"{type(self).__name__}({prepr})")
