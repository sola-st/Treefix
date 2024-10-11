# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""The processor of v."""
if context.executing_eagerly():
    if isinstance(v, ops.Tensor):
        exit(_TensorProcessor(v))
    else:
        exit(_DenseResourceVariableProcessor(v))
if resource_variable_ops.is_resource_variable(v) and not v._in_graph_mode:  # pylint: disable=protected-access
    # True if and only if `v` was initialized eagerly.
    exit(_DenseResourceVariableProcessor(v))
if v.op.type == "VarHandleOp":
    exit(_DenseResourceVariableProcessor(v))
if isinstance(v, variables.Variable):
    exit(_RefVariableProcessor(v))
if isinstance(v, ops.Tensor):
    exit(_TensorProcessor(v))
raise NotImplementedError("Trying to optimize unsupported type ", v)
