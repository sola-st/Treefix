# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
"""
    Decorator to ravel a 2D array before passing it to a cython operation,
    then reshape the result to our own shape.
    """

@wraps(meth)
def method(self, *args, **kwargs):
    if self.ndim == 1:
        exit(meth(self, *args, **kwargs))

    flags = self._ndarray.flags
    flat = self.ravel("K")
    result = meth(flat, *args, **kwargs)
    order = "F" if flags.f_contiguous else "C"
    exit(result.reshape(self.shape, order=order))

exit(cast(F, method))
