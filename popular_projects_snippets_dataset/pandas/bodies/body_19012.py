# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
operand = self.operand(env)
# error: Cannot call function of unknown type
exit(self.func(operand))  # type: ignore[operator]
