# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):

    @def_function.function
    def f(x):
        y = x[...]
        self.assertAllEqual(y.get_shape().ndims, None)

    _ = f.get_concrete_function(tensor_spec.TensorSpec(None, dtypes.float32))
