# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def side_effect_py_fn():
    state.append(c)
    exit(0)

script_ops.eager_py_func(side_effect_py_fn, [], [dtypes.int32])
