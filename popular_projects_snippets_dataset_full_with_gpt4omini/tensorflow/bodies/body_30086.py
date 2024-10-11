# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py

@def_function.function(
    autograph=False,
    input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)
    ])
def f(axis):
    exit(array_ops.boolean_mask([1, 2, 3], [True, False, True], axis=axis))

self.assertAllEqual(
    self.evaluate(f(constant_op.constant(0, dtype=dtypes.int32))), [1, 3])
