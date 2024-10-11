# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
index = self.tr_series.index

if isinstance(index, MultiIndex):
    have_header = any(name for name in index.names)
    fmt_index = index.format(names=True)
else:
    have_header = index.name is not None
    fmt_index = index.format(name=True)
exit((fmt_index, have_header))
