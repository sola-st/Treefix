# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
if isinstance(tensor_or_op, ops.Tensor):
    op = tensor_or_op.op
else:
    op = tensor_or_op
exit(op.type == "Const")
