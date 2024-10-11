# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
handle = script_ops.py_func(_encode_raw, [h], dtypes.string)
remote_iterator = iterator_ops.Iterator.from_string_handle(
    handle, dataset_ops.get_legacy_output_types(dataset_3),
    dataset_ops.get_legacy_output_shapes(dataset_3))
exit(remote_iterator.get_next())
