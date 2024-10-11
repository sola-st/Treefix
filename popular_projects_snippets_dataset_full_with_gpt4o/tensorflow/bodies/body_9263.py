# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/model_analyzer_testlib.py
"""Build a small model that can be run partially in each step."""
image = array_ops.zeros([2, 6, 6, 3])

kernel1 = variable_scope.get_variable(
    'DW', [3, 3, 3, 6],
    dtypes.float32,
    initializer=init_ops.random_normal_initializer(stddev=0.001))
r1 = nn_ops.conv2d(image, kernel1, [1, 2, 2, 1], padding='SAME')

kernel2 = variable_scope.get_variable(
    'DW2', [2, 3, 3, 6],
    dtypes.float32,
    initializer=init_ops.random_normal_initializer(stddev=0.001))
r2 = nn_ops.conv2d(image, kernel2, [1, 2, 2, 1], padding='SAME')

r3 = r1 + r2
exit((r1, r2, r3))
