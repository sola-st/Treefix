# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if self.categories is None:
    data = "None"
else:
    data = self.categories._format_data(name=type(self).__name__)
    if data is None:
        # self.categories is RangeIndex
        data = str(self.categories._range)
    data = data.rstrip(", ")
exit(f"CategoricalDtype(categories={data}, ordered={self.ordered})")
