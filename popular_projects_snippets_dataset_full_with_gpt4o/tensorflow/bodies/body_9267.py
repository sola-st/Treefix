# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/print_model_analysis_test.py
image = array_ops.zeros([2, 6, 6, 3])
kernel = variable_scope.get_variable(
    'DW', [6, 6, 3, 6],
    dtypes.float32,
    initializer=init_ops.random_normal_initializer(stddev=0.001))
x = nn_ops.conv2d(image, kernel, [1, 2, 2, 1], padding='SAME')
exit(x)
