# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
dataset = build_dataset(sparse=no_padding)
dataset = dataset.bucket_by_sequence_length(
    element_length_func=_element_length_fn,
    bucket_batch_sizes=[2, 2, 2],
    bucket_boundaries=[0, 8],
    no_padding=no_padding)
shapes = dataset_ops.get_legacy_output_shapes(dataset)
self.assertEqual([None, None], shapes[0].as_list())
self.assertEqual([None], shapes[1].as_list())
