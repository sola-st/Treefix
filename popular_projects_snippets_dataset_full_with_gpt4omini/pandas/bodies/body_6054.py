# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
op = self.get_op_from_name(op_name)

self._check_op(ser, op, other, op_name, exc)
