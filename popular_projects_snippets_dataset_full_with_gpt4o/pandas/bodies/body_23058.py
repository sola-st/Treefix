# Extracted from ./data/repos/pandas/pandas/core/generic.py

inplace = validate_bool_kwarg(inplace, "inplace")
cond = common.apply_if_callable(cond, self)

# see gh-21891
if not hasattr(cond, "__invert__"):
    cond = np.array(cond)

exit(self.where(
    ~cond,
    other=other,
    inplace=inplace,
    axis=axis,
    level=level,
))
