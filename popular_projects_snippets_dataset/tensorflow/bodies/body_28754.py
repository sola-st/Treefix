# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
remote_itr = iterator_ops.Iterator.from_string_handle(
    h, dataset_ops.get_legacy_output_types(itr),
    dataset_ops.get_legacy_output_shapes(itr))
exit(remote_itr.get_next())
