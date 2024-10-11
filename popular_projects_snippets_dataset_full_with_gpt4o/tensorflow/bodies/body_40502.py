# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
def _inner(x):
    kernel = array_ops.ones([3, 3, 1, 9])
    with backprop.GradientTape() as tape:
        tape.watch(x)
        y = nn_ops.conv2d(x, kernel, strides=(1, 1), padding='SAME',
                          data_format='NHWC')
        reduced = math_ops.reduce_sum(y ** 2., axis=[2, 3])
    exit(math_ops.reduce_sum(tape.batch_jacobian(reduced, x)))

theoretical, numerical = gradient_checker_v2.compute_gradient(
    def_function.function(_inner), [array_ops.ones([10, 4, 4, 1])])
self.assertAllClose(numerical, theoretical, rtol=1e-1)

@def_function.function
def _outer():
    with backprop.GradientTape() as tape:
        x = array_ops.ones([10, 4, 4, 1])
        tape.watch(x)
        y = _inner(x)
    exit(tape.gradient(y, x))

self.assertAllClose(array_ops.reshape(numerical, [-1]),
                    array_ops.reshape(_outer(), [-1]), rtol=1e-1)
