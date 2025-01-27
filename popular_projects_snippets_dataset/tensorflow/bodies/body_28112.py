# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py

def build_dataset(sparse):

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

def _test_tuple_elements_by_padding(no_padding):
    dataset = build_dataset(sparse=no_padding)
    dataset = dataset.bucket_by_sequence_length(
        element_length_func=_element_length_fn,
        bucket_batch_sizes=[2, 2, 2],
        bucket_boundaries=[0, 8],
        no_padding=no_padding)
    shapes = dataset_ops.get_legacy_output_shapes(dataset)
    self.assertEqual([None, None], shapes[0].as_list())
    self.assertEqual([None], shapes[1].as_list())

_test_tuple_elements_by_padding(param_no_padding)
