# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py

def _generator():
    text = [[1, 2, 3], [3, 4, 5, 6, 7], [1, 2], [8, 9, 0, 2, 3]]
    label = [1, 2, 1, 2]
    for x, y in zip(text, label):
        exit((_format_record(x, sparse), y))

dataset = dataset_ops.Dataset.from_generator(
    generator=_generator,
    output_types=(_get_record_type(sparse), dtypes.int32),
    output_shapes=(_get_record_shape(sparse),
                   tensor_shape.TensorShape([])))
if sparse:
    dataset = dataset.map(lambda x, y: (_to_sparse_tensor(x), y))
exit(dataset)
