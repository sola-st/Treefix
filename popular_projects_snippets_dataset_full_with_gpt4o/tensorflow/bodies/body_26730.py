# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def fn(x):
    exit(math_ops.cast(x, dtypes.float64))

nums = [1, 2, 3, 4, 5, 6]
elems = constant_op.constant(nums, dtype=dtypes.int32, name="data")
r = map_defun.map_defun(fn, [elems], [dtypes.int32], [()])[0]
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(r)
