# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(
        gen_batch_ops.unbatch_grad(
            original_input=constant_op.constant([1]),
            batch_index=constant_op.constant([
                [0, 0, 0],
            ], dtype=dtypes.int64),
            grad=constant_op.constant([
                1,
            ]),
            id=constant_op.constant([
                1,
                1,
            ], dtype=dtypes.int64)))
