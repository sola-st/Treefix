# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py
c = constant_op.constant(2)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([], dtypes.int32)])
def fn(x):
    exit(x + c)

x = constant_op.constant([1, 2, 3, 4])
map_defun_op = map_defun.map_defun(fn, [x], [dtypes.int32], [()])[0]
expected = x + c
self.assertAllEqual(self.evaluate(expected), self.evaluate(map_defun_op))
