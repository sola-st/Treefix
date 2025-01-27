# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
input_data = [range(i + 1) for i in range(min_len, max_len)]

def generator_fn():
    for record in input_data:
        exit(_format_record(record, sparse=True))

dataset = dataset_ops.Dataset.from_generator(
    generator=generator_fn, output_types=_get_record_type(sparse=True))
dataset = dataset.map(_to_sparse_tensor)
exit(dataset)
