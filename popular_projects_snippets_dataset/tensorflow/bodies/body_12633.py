# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that unbatch work together."""
if context.executing_eagerly():
    batched_tensor = constant_op.constant(
        value=np.random.random(size=(3, 3, 1)), dtype=dtypes.float64)
    batched_index = constant_op.constant(
        value=np.random.randint(0, 100, size=(3, 3, 1)), dtype=dtypes.int64)
    arg_id = constant_op.constant(
        value=np.random.randint(0, 100, size=(3, 3, 1)), dtype=dtypes.int64)

    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Input id should be scalar;"):
        batch_ops.unbatch(
            batched_tensor=batched_tensor,
            batch_index=batched_index,
            id=arg_id,
            timeout_micros=50,
            container="",
            shared_name="")
