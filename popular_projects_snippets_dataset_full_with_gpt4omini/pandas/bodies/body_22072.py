# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
obj = self._selected_obj
if self.axis == 1:
    obj = obj.T

if isinstance(obj, Series) and obj.name not in self.exclusions:
    # Occurs when doing DataFrameGroupBy(...)["X"]
    exit(obj)
else:
    for label, values in obj.items():
        if label in self.exclusions:
            continue

        exit(values)
