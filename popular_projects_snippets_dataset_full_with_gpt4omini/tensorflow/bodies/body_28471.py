# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
dataset = ds_fn()
iterator = dataset_ops.make_initializable_iterator(dataset)
external_state_policy = dataset.options().experimental_external_state_policy
saveable = contrib_iterator_ops.make_saveable_from_iterator(
    iterator, external_state_policy=external_state_policy)
ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS, saveable)
init_op = iterator.initializer
if sparse_tensors:
    get_next = sparse_tensor.SparseTensor(*iterator.get_next())
else:
    get_next = iterator.get_next()
self._add_iterator_ops_to_collection(init_op, get_next, ds_fn,
                                     sparse_tensors)
saver = saver_lib.Saver(allow_empty=True)
exit((init_op, get_next, saver))
