# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([2], dtypes.int32)])
def fn(x):
    exit(x)

elems = array_ops.placeholder(dtypes.int64, (None, 2))
result = map_defun.map_defun(fn, [elems], [dtypes.int32], [(2,)])
self.assertEqual(result[0].get_shape().as_list(), [None, 2])
