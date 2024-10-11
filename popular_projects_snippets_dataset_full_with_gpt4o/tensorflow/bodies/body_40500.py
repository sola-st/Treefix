# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
kernel = array_ops.ones([3, 3, 1, 9])
with backprop.GradientTape() as tape:
    tape.watch(x)
    y = nn_ops.conv2d(x, kernel, strides=(1, 1), padding='SAME',
                      data_format='NHWC')
    reduced = math_ops.reduce_sum(y ** 2., axis=[2, 3])
exit(math_ops.reduce_sum(tape.batch_jacobian(reduced, x)))
