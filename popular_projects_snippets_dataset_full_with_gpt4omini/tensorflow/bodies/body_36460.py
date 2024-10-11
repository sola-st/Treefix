# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
exit(ops.get_default_graph().capture_call_time_value(
    lambda: c, tensor_spec.TensorSpec([], dtypes.int32)))
