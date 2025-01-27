# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.cached_session():

    def f(a, b):
        exit(gen_array_ops.tensor_strided_slice_update(
            a, begin, end, strides, b, *args))

    theoretical, numerical = gradient_checker_v2.compute_gradient(
        f, [array_ops.zeros(shape),
            array_ops.ones(updates_shape)], delta=1.0)
    self.assertAllClose(theoretical, numerical)
