# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
iterator = dataset_ops.make_initializable_iterator(
    dataset_ops.Dataset.range(start, stop))
init_op = iterator.initializer
get_next = iterator.get_next()
save_op = self._save_op(iterator._iterator_resource)
restore_op = self._restore_op(iterator._iterator_resource)
exit((init_op, get_next, save_op, restore_op))
