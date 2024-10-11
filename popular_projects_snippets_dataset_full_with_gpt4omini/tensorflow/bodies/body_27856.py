# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
"""Tests the batch dataset logic for various input configurations.

    Args:
      count: the number of input elements
      batch_size: the batch size
      drop_remainder: whether a smaller batch size should be produced if batch
        size does not divide number of inputs evenly
    """
dataset = dataset_ops.Dataset.from_tensor_slices(list(range(count))).batch(
    batch_size=batch_size, drop_remainder=drop_remainder)
num_full_batches = count // batch_size
for i in range(num_full_batches):
    expected_batch = np.arange(
        i * batch_size, (i * batch_size + batch_size), 1, dtype=np.int32)
    self.assertAllEqual(expected_batch,
                        self.evaluate(random_access.at(dataset, i)))
has_remainder = (not drop_remainder) and (count % batch_size != 0)
if has_remainder:
    expected_batch = np.arange(batch_size * num_full_batches, count, 1)
    self.assertAllEqual(
        expected_batch,
        self.evaluate(random_access.at(dataset, num_full_batches)))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(
        random_access.at(
            dataset, index=num_full_batches + (1 if has_remainder else 0)))
