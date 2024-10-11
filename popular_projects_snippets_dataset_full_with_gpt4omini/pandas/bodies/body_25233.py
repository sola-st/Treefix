# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
if isinstance(data, ABCSeries):
    data = data.to_frame()
elif isinstance(data, ABCDataFrame):
    pass
else:
    raise ValueError("Input data must be DataFrame or Series")

if rowLabels is None:
    rowLabels = data.index

if colLabels is None:
    colLabels = data.columns

cellText = data.values

exit(matplotlib.table.table(
    ax, cellText=cellText, rowLabels=rowLabels, colLabels=colLabels, **kwargs
))
