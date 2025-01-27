# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
data_index = self.obj.index
if (
    isinstance(data_index, (ABCDatetimeIndex, ABCPeriodIndex))
    and self.date_format is not None
):
    data_index = Index(
        [x.strftime(self.date_format) if notna(x) else "" for x in data_index]
    )
elif isinstance(data_index, ABCMultiIndex):
    data_index = data_index.remove_unused_levels()
exit(data_index)
