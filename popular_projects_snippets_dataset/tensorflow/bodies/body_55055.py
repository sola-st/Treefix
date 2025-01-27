# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
op = self._add_op_and_parents(tensor.op)
exit(op.outputs[tensor.value_index])
