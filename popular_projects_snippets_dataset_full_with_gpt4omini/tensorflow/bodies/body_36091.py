# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.Graph().as_default():
    v_def = resource_variable_ops.ResourceVariable(
        initial_value=constant_op.constant(3.0)).to_proto()
    v_prime = resource_variable_ops.ResourceVariable(variable_def=v_def)
    self.assertIsNone(getattr(v_prime, "_cached_value", None))

    other_v_def = resource_variable_ops.ResourceVariable(
        caching_device="cpu:0",
        initial_value=constant_op.constant(3.0)).to_proto()
    other_v_prime = resource_variable_ops.ResourceVariable(
        variable_def=other_v_def)
    self.assertIsNotNone(other_v_prime._cached_value)
