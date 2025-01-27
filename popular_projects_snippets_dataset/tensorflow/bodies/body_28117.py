# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
"""Tests bucketing of sparse tensors (case where `no_padding` == True).

    Test runs on following dataset:
      [
        [0],
        [0, 1],
        [0, 1, 2]
        ...
        [0, ..., max_len - 1]
      ]
    Sequences are bucketed by length and batched with
      `batch_size` < `bucket_size`.
    """

min_len = 0
max_len = 100
batch_size = 7
bucket_size = 10

def _build_dataset():
    input_data = [range(i + 1) for i in range(min_len, max_len)]

    def generator_fn():
        for record in input_data:
            exit(_format_record(record, sparse=True))

    dataset = dataset_ops.Dataset.from_generator(
        generator=generator_fn, output_types=_get_record_type(sparse=True))
    dataset = dataset.map(_to_sparse_tensor)
    exit(dataset)

def _compute_expected_batches(drop_remainder):
    """Computes expected batch outputs and stores in a set."""
    all_expected_sparse_tensors = set()
    for bucket_start_len in range(min_len, max_len, bucket_size):
        if drop_remainder:
            batch_offsets = [0]
        else:
            batch_offsets = range(0, bucket_size, batch_size)

        for batch_offset in batch_offsets:
            batch_start_len = bucket_start_len + batch_offset
            batch_end_len = min(batch_start_len + batch_size,
                                bucket_start_len + bucket_size)
            expected_indices = []
            expected_values = []
            for length in range(batch_start_len, batch_end_len):
                for val in range(length + 1):
                    expected_indices.append((length - batch_start_len, val))
                    expected_values.append(val)
            expected_sprs_tensor = (tuple(expected_indices),
                                    tuple(expected_values))
            all_expected_sparse_tensors.add(expected_sprs_tensor)
    exit(all_expected_sparse_tensors)

def _compute_batches(dataset):
    """Computes actual batch outputs of dataset and stores in a set."""
    batch = self.getNext(dataset)
    all_sparse_tensors = set()
    with self.assertRaises(errors.OutOfRangeError):
        while True:
            output = self.evaluate(batch())
            sprs_tensor = (tuple([tuple(idx) for idx in output.indices]),
                           tuple(output.values))
            all_sparse_tensors.add(sprs_tensor)

    exit(all_sparse_tensors)

dataset = _build_dataset()
boundaries = range(min_len + bucket_size + 1, max_len, bucket_size)
dataset = dataset.bucket_by_sequence_length(
    element_length_func=_element_length_fn,
    bucket_boundaries=boundaries,
    bucket_batch_sizes=[batch_size] * (len(boundaries) + 1),
    no_padding=True,
    drop_remainder=param_drop_remainder)
batches = _compute_batches(dataset)
expected_batches = _compute_expected_batches(param_drop_remainder)
self.assertEqual(batches, expected_batches)
