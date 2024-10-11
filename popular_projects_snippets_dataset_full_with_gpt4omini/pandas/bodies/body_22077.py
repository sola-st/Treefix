# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
exit(self.grouper._cython_operation(
    "transform", bvalues, how, 1, **kwargs
))
