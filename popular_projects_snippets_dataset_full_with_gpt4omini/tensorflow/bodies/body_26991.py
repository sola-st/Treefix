# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
"""Test a dataset that maps a TF function across its input elements."""

with self.assertRaisesRegex(errors.InvalidArgumentError, "oops"):
    dataset = dataset_ops.Dataset.from_tensors(
        array_ops.check_numerics(
            constant_op.constant(1.0) / constant_op.constant(0.0), "oops"))
    dataset = dataset.apply(batching.map_and_batch(lambda x: x, 14))
    get_next = self.getNext(dataset, requires_initialization=True)
    self.evaluate(get_next())
