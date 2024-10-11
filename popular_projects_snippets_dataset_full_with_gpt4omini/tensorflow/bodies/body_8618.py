# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
with self.device:
    x = constant_op.constant([1., 2.])
    x = array_ops.identity(x)

    @def_function.function
    def f(y):
        exit(x + y)

    y = array_ops.ones([2])
    parallel_result = f(y)
self.assertAllClose([[2., 3.]] * 2, self.device.unpack(parallel_result))
