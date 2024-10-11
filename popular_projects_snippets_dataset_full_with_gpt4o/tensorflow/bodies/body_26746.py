# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([2], dtypes.int32)])
def simple_fn(x):
    res = x * 2 + 3
    exit((res, res + 1, res + 2))

nums = [[1, 2], [3, 4], [5, 6]]
elems = constant_op.constant(nums, dtype=dtypes.int32, name="data")
r = map_defun.map_defun(simple_fn, [elems],
                        [dtypes.int32, dtypes.int32, dtypes.int32],
                        [None, (None,), (2,)])
expected = elems * 2 + 3
self.assertAllEqual(self.evaluate(r[0]), self.evaluate(expected))
self.assertAllEqual(self.evaluate(r[1]), self.evaluate(expected + 1))
self.assertAllEqual(self.evaluate(r[2]), self.evaluate(expected + 2))
