# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
remote_iterator = iterator_ops.Iterator.from_string_handle(
    h, dataset_ops.get_legacy_output_types(dataset_3),
    dataset_ops.get_legacy_output_shapes(dataset_3))
exit(remote_iterator.get_next())
