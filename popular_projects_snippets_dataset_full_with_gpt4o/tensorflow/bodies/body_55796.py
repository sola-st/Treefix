# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
script_ops.eager_py_func(side_effect_one, [1], [dtypes.int32])
script_ops.eager_py_func(side_effect_two, [1], [dtypes.int32])
exit(1)
