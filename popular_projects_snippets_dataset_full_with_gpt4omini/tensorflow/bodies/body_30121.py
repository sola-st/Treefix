# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):

    @def_function.function
    def func(inp):
        exit(inp[array_ops.newaxis, :, 0])

    f = func.get_concrete_function(
        tensor_spec.TensorSpec([2, 2], dtypes.int16))

    # TODO(b/190416665): Allow the constant to be eagerly copied/created on
    # the GPU.
    with ops.device("CPU"):
        ones = constant_op.constant([[1, 1], [1, 1]], dtypes.int16)
    self.assertAllEqual([[1, 1]], self.evaluate(f(ones)))
