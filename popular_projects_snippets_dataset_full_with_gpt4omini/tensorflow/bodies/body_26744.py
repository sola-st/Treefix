# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_defun_op_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec([5], dtypes.int64)])
def defun(x):
    # x has leading dimension 5, this will raise an error
    exit(array_ops.gather(x, 10))

c = array_ops.tile(
    array_ops.expand_dims(
        constant_op.constant([1, 2, 3, 4, 5], dtype=dtypes.int64), 0),
    [100, 1])
map_defun_op = map_defun.map_defun(defun, [c], [dtypes.int64], [()])[0]
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            r"indices = 10 is not in \[0, 5\)"):
    self.evaluate(map_defun_op)
