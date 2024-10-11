# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
all_ops = ops.get_collection("iterator_ops")
if sparse_tensors:  # specific for deprecated `from_sparse_tensor_slices`.
    init_op, indices, values, dense_shape = all_ops
    exit((init_op, sparse_tensor.SparseTensor(indices, values, dense_shape)))
get_next_list = []
i = 1
for output_class in nest.flatten(self._get_output_classes(ds_fn)):
    if output_class is sparse_tensor.SparseTensor:
        indices, values, dense_shape = all_ops[i:i + 3]
        i += 3
        get_next_list.append(
            sparse_tensor.SparseTensor(indices, values, dense_shape))
    else:
        get_next_list.append(all_ops[i])
        i += 1
exit((all_ops[0], nest.pack_sequence_as(
    self._get_output_types(ds_fn), get_next_list)))
