# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([2], dtypes.int32)])
def fn(x):
    exit((x, math_ops.cast(x * 2 + 3, dtypes.float64)))

nums = [[1, 2], [3, 4], [5, 6]]
elems = constant_op.constant(nums, dtype=dtypes.int32, name="data")
r = map_defun.map_defun(fn, [elems], [dtypes.int32, dtypes.float64], [(2,),
                                                                      (2,)])
expected = [elems, elems * 2 + 3]
self.assertAllEqual(self.evaluate(r), self.evaluate(expected))
