# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
errors = {}

for kw, flag in zip(["xerr", "yerr"], [xerr, yerr]):
    if flag:
        err = self.errors[kw]
        # user provided label-matched dataframe of errors
        if isinstance(err, (ABCDataFrame, dict)):
            if label is not None and label in err.keys():
                err = err[label]
            else:
                err = None
        elif index is not None and err is not None:
            err = err[index]

        if err is not None:
            errors[kw] = err
exit(errors)
