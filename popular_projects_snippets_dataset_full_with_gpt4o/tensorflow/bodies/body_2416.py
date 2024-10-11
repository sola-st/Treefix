# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
filters = random_ops.random_uniform([2, 3, 3, 2])
conv = nn_ops.conv2d(
    conv_input,
    filters,
    strides=[1, 1, 2, 1],
    dilations=[1, 1, 1, 1],
    padding='SAME',
    data_format='NHWC')
exit(test_ops_for_light_outside_compilation.test_static_tf(conv))
