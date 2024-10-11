# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
original_input = random_ops.random_uniform(
    shape=(3, 1), dtype=dtypes.float64, maxval=None)
batch_index = random_ops.random_uniform(
    shape=(3, 1), dtype=dtypes.int64, maxval=65536)
grad = random_ops.random_uniform(
    shape=(3, 1), dtype=dtypes.float64, maxval=None)
batch_id = random_ops.random_uniform(
    shape=(3, 1), dtype=dtypes.int64, maxval=65536)
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(
        gen_batch_ops.unbatch_grad(
            original_input=original_input,
            batch_index=batch_index,
            grad=grad,
            id=batch_id,
            container="",
            shared_name="",
            name=""))
