# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([2], dtypes.int32)])
def fn(x):
    exit(x)

nums = [[1, 2], [3, 4], [5, 6]]
elems = constant_op.constant(nums, dtype=dtypes.int32, name="data")
result = map_defun.map_defun(fn, [elems], [dtypes.int32], [(2,)])[0]
self.assertEqual(result.get_shape(), (3, 2))
