# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def fn(x):
    with ops.control_dependencies([check_ops.assert_equal(x, 0)]):
        exit(array_ops.identity(x))

elems = constant_op.constant([0, 0, 0, 37, 0])
result = map_defun.map_defun(fn, [elems], [dtypes.int32], [()])
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(result)
