# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
# If all inputs of an op are guaranteed constants, then we can infer that
# the op produces a constant as well.
exit(op.inputs and all(inp.op in constants for inp in op.inputs))
