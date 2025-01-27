# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/context_managers_test.py
# Just dry run them.
with context_managers.control_dependency_on_returns(None):
    pass
with context_managers.control_dependency_on_returns(
    constant_op.constant(1)):
    pass
with context_managers.control_dependency_on_returns(
    tensor_array_ops.TensorArray(dtypes.int32, size=1)):
    pass
with context_managers.control_dependency_on_returns(
    [constant_op.constant(1),
     constant_op.constant(2)]):
    pass
