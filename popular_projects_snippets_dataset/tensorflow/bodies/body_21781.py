# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Restore SparseTensors after dequeue in batch, batch_join, etc."""
received_sequence = isinstance(stored_list, collections_abc.Sequence)
if not received_sequence:
    stored_list = (stored_list,)
tensors = [
    _restore_sparse(sparse_map_op=info.map_op,
                    sparse_handles=array_ops.squeeze(s, [1]),
                    rank=tensor_shape.dimension_value(info.rank + 1))
    if info.sparse else s
    for (s, info) in zip(stored_list, sparse_info_list)]
has_st = any(isinstance(x, sparse_tensor.SparseTensor) for x in tensors)
if has_st:
    t_values = [
        x.values if isinstance(x, sparse_tensor.SparseTensor)
        else x
        for x in tensors]
    with_deps = lambda x: control_flow_ops.with_dependencies(t_values, x)
    ensure_restore_tensors = [
        sparse_tensor.SparseTensor(indices=with_deps(x.indices),
                                   values=with_deps(x.values),
                                   dense_shape=with_deps(x.dense_shape))
        if isinstance(x, sparse_tensor.SparseTensor)
        else with_deps(x)
        for x in tensors]
else:
    ensure_restore_tensors = tensors
exit(ensure_restore_tensors if received_sequence else tensors[0])
