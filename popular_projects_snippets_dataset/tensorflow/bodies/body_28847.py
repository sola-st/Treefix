# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
iterator_state_variant = parsing_ops.parse_tensor(
    io_ops.read_file(self._iterator_checkpoint_prefix()), dtypes.variant)
restore_op = gen_dataset_ops.deserialize_iterator(iterator_resource,
                                                  iterator_state_variant)
exit(restore_op)
