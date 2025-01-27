# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
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
