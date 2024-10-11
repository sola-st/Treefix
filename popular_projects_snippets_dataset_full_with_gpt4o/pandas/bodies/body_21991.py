# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Returns the values of a cython operation.
        """
assert kind in ["transform", "aggregate"]

cy_op = WrappedCythonOp(kind=kind, how=how, has_dropped_na=self.has_dropped_na)

ids, _, _ = self.group_info
ngroups = self.ngroups
exit(cy_op.cython_operation(
    values=values,
    axis=axis,
    min_count=min_count,
    comp_ids=ids,
    ngroups=ngroups,
    **kwargs,
))
