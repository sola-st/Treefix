# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
dataset = build_dataset(sparse=no_padding)
dataset = dataset.bucket_by_sequence_length(
    element_length_func=_element_length_fn,
    bucket_boundaries=boundaries,
    bucket_batch_sizes=batch_sizes,
    no_padding=no_padding,
    drop_remainder=True)

get_next = self.getNext(dataset)
batches = []
for _ in range(n_expected_batches):
    batch, = self.evaluate(get_next())
    batches.append(batch)

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

generated_lengths = []

# <seq-length>: <total-sum>
generated_sums = {}

# <seq-length>: [<batch_size>, ...]
generated_batch_sizes = {}

for length, batch_size, bucket_elements in zip(lengths, batch_sizes,
                                               n_bucket_elements):
    # Initialize the sum across all batches.
    generated_sums[length] = 0
    # Initialize the individual batch sizes.
    generated_batch_sizes[length] = []

for batch in batches:
    shape = batch.dense_shape if no_padding else batch.shape
    length = shape[1]
    generated_lengths.append(length)

    batch_size = shape[0]
    generated_batch_sizes[length].append(batch_size)

    batch_sum = batch.values.sum() if no_padding else batch.sum()
    generated_sums[length] += batch_sum

for l in lengths:
    # Make sure the sum of the batch contents is correct for the individual
    # sequence lengths.
    self.assertEqual(
        generated_sums[l], expected_sums[l], "Tensor sums did not match! "
        "expected: {}, generated: {}".format(expected_sums, generated_sums))

    # Make sure the individual batch sizes are generated as expected.
    self.assertEqual(
        sorted(generated_batch_sizes[l]), sorted(expected_batch_sizes[l]),
        "Batch-sizes did not match! "
        "expected: {}, generated: {}".format(
            sorted(expected_batch_sizes[l]),
            sorted(generated_batch_sizes[l])))

# Make sure the generated sequence lengths appear as often as expected.
self.assertEqual(
    sorted(generated_lengths), sorted(expected_lengths),
    "The generated sequence lengths did not match! "
    "expected: {}, generated: {}".format(
        sorted(expected_lengths), sorted(generated_lengths)))
