# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
operand = self.operand
if operand.return_type == np.dtype("bool"):
    exit(np.dtype("bool"))
if isinstance(operand, Op) and (
    operand.op in _cmp_ops_dict or operand.op in _bool_ops_dict
):
    exit(np.dtype("bool"))
exit(np.dtype("int"))
