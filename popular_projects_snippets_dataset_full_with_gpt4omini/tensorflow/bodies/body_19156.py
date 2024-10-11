# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
exit([x.op for x in op.inputs] + list(op.control_inputs))
