# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
# error: "Op" not callable
operands = [op(env) for op in self.operands]  # type: ignore[operator]
with np.errstate(all="ignore"):
    exit(self.func.func(*operands))
