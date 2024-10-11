# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/grappler_test.py
features = {"x": parsing_ops.VarLenFeature(dtypes.int64)}
parsed = parsing_ops.parse_single_example(serialized, features)
parsed = parsed["x"].values

size = array_ops.size(parsed)
value = math_ops.cast(parsed, dtypes.bool)
exit(control_flow_ops.cond(size > 0,
                             lambda: array_ops.reshape(value, []),
                             lambda: array_ops.zeros([], dtypes.bool)))
