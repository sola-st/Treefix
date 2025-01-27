# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/constant_folding_test.py
x = array_ops.zeros([10, 20, 30], dtype=dtypes.float32)
x = functional_ops.scan(
    math_ops.add,
    x,
    initializer=array_ops.zeros([20, 30], dtype=dtypes.float32),
    back_prop=False,
    parallel_iterations=1)

with ops.device('/cpu:0'):
    y = array_ops.identity(x)

    exit((idx_step + 1, y))
