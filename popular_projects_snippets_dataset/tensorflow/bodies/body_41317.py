# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
exit(control_flow_ops.cond(
    array_ops.placeholder_with_default(True, ()), v.read_value,
    v.read_value))
