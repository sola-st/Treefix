# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
dataset = build_dataset(sparse=no_padding)
dataset = dataset.bucket_by_sequence_length(
    element_length_func=_element_length_fn,
    bucket_boundaries=boundaries,
    bucket_batch_sizes=batch_sizes,
    no_padding=no_padding)
get_next = self.getNext(dataset)
batches = []
for _ in range(4):
    batch, = self.evaluate(get_next())
    batches.append(batch)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

batch_sizes_val = []
lengths_val = []
for batch in batches:
    shape = batch.dense_shape if no_padding else batch.shape
    batch_size = shape[0]
    length = shape[1]
    batch_sizes_val.append(batch_size)
    lengths_val.append(length)
    if not context.executing_eagerly():
        sum_check = batch.values.sum() if no_padding else batch.sum()
        self.assertEqual(sum_check, batch_size * length - 1)
self.assertEqual(sum(batch_sizes_val), sum(batch_sizes))
self.assertEqual(sorted(batch_sizes), sorted(batch_sizes_val))
self.assertEqual(sorted(lengths), sorted(lengths_val))
