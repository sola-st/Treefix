# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
    If we have a multi-column block, split and operate block-wise.  Otherwise
    use the original method.
    """

@wraps(meth)
def newfunc(self, *args, **kwargs) -> list[Block]:

    if self.ndim == 1 or self.shape[0] == 1:
        exit(meth(self, *args, **kwargs))
    else:
        # Split and operate column-by-column
        exit(self.split_and_operate(meth, *args, **kwargs))

exit(cast(F, newfunc))
