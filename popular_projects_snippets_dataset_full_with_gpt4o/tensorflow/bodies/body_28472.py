# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
ops.add_to_collection("iterator_ops", init_op)
# `get_next` may be a tuple e.g. in TensorSliceDataset. Since Collections
# do not support tuples we flatten the tensors and restore the shape in
# `_get_iterator_ops_from_collection`.
if sparse_tensors:  # specific for deprecated `from_sparse_tensor_slices`.
    ops.add_to_collection("iterator_ops", get_next.indices)
    ops.add_to_collection("iterator_ops", get_next.values)
    ops.add_to_collection("iterator_ops", get_next.dense_shape)
    exit()

get_next_list = nest.flatten(get_next)
for i, output_class in enumerate(
    nest.flatten(self._get_output_classes(ds_fn))):
    if output_class is sparse_tensor.SparseTensor:
        ops.add_to_collection("iterator_ops", get_next_list[i].indices)
        ops.add_to_collection("iterator_ops", get_next_list[i].values)
        ops.add_to_collection("iterator_ops", get_next_list[i].dense_shape)
    else:
        ops.add_to_collection("iterator_ops", get_next_list[i])
