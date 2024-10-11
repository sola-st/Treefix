# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/datasets.py
remote_iterator = iterator_ops.Iterator.from_string_handle(
    h, dataset_ops.get_legacy_output_types(source_dataset),
    dataset_ops.get_legacy_output_shapes(source_dataset))
exit(remote_iterator.get_next())
