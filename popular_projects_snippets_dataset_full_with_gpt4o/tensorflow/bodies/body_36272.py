# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
@function.Defun(dtypes.int32)
def AddFive(x):
    exit(x + 5)

op = functional_ops.partitioned_call(
    args=[constant_op.constant([1, 2, 3], dtype=dtypes.int32)],
    f=AddFive,
    executor_type="NON_EXISTENT_EXECUTOR")
with self.assertRaisesRegex(errors.NotFoundError, "NON_EXISTENT_EXECUTOR"):
    self.evaluate(op)
