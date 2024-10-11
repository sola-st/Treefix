# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
unique = series.unique()
# unique and colors length can be differed
# depending on slice value
mapped = dict(zip(unique, colors))
exit([mapped[v] for v in series.values])
