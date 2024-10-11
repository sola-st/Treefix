# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
iterator_state_variant = gen_dataset_ops.serialize_iterator(
    iterator_resource)
save_op = io_ops.write_file(
    self._iterator_checkpoint_prefix(),
    parsing_ops.serialize_tensor(iterator_state_variant))
exit(save_op)
