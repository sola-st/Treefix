# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/model_analyzer_testlib.py
"""Build a small forward conv model."""
image = array_ops.zeros([2, 6, 6, 3])
_ = variable_scope.get_variable(
    'ScalarW', [],
    dtypes.float32,
    initializer=init_ops.random_normal_initializer(stddev=0.001))
kernel = variable_scope.get_variable(
    'DW', [3, 3, 3, 6],
    dtypes.float32,
    initializer=init_ops.random_normal_initializer(stddev=0.001))
x = nn_ops.conv2d(image, kernel, [1, 2, 2, 1], padding='SAME')
kernel = variable_scope.get_variable(
    'DW2', [2, 2, 6, 12],
    dtypes.float32,
    initializer=init_ops.random_normal_initializer(stddev=0.001))
x = nn_ops.conv2d(x, kernel, [1, 2, 2, 1], padding='SAME')
exit(x)
