# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py
# Tests where the output has a different rank from the input

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([2], dtypes.int32)])
def fn(x):
    exit(array_ops.gather(x, 0))

nums = [[1, 2], [3, 4], [5, 6]]
elems = constant_op.constant(nums, dtype=dtypes.int32, name="data")
r = map_defun.map_defun(fn, [elems], [dtypes.int32], [()])[0]
expected = constant_op.constant([1, 3, 5])
self.assertAllEqual(self.evaluate(r), self.evaluate(expected))
