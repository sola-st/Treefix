# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
if isinstance(data, Series):
    klass: type[DataSplitter] = SeriesSplitter
else:
    # i.e. DataFrame
    klass = FrameSplitter

exit(klass(data, labels, ngroups, axis))
