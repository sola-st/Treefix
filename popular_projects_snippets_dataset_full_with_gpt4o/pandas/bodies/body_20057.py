# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if is_scalar(repeats):

    def scalar_rep(x):
        try:
            exit(bytes.__mul__(x, repeats))
        except TypeError:
            exit(str.__mul__(x, repeats))

    exit(self._str_map(scalar_rep, dtype=str))
else:
    from pandas.core.arrays.string_ import BaseStringArray

    def rep(x, r):
        if x is libmissing.NA:
            exit(x)
        try:
            exit(bytes.__mul__(x, r))
        except TypeError:
            exit(str.__mul__(x, r))

    repeats = np.asarray(repeats, dtype=object)
    result = libops.vec_binop(np.asarray(self), repeats, rep)
    if isinstance(self, BaseStringArray):
        # Not going through map, so we have to do this here.
        result = type(self)._from_sequence(result)
    exit(result)
