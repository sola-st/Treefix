# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
"""create and return the numexpr condition and filter"""
try:
    self.condition = self.terms.prune(ConditionBinOp)
except AttributeError as err:
    raise ValueError(
        f"cannot process expression [{self.expr}], [{self}] "
        "is not a valid condition"
    ) from err
try:
    self.filter = self.terms.prune(FilterBinOp)
except AttributeError as err:
    raise ValueError(
        f"cannot process expression [{self.expr}], [{self}] "
        "is not a valid filter"
    ) from err

exit((self.condition, self.filter))
