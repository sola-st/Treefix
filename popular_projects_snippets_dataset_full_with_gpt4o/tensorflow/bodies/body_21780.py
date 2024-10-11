# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Store SparseTensors for feeding into batch_join, etc."""
(s0, sparse_info_list) = _store_sparse_tensors(
    tensor_list_list[0], enqueue_many, keep_input)
stored_list_list = [s0]
for tensor_list in tensor_list_list[1:]:
    s, sparse_info_candidate = _store_sparse_tensors(
        tensor_list, enqueue_many, keep_input,
        [st.map_op for st in sparse_info_list])
    if sparse_info_list != sparse_info_candidate:
        raise ValueError("Inconsistent SparseTensors list: %s vs. %s"
                         % (tensor_list_list[0], tensor_list))
    sparse_info_list = [
        info.merge_with(candidate)
        for (info, candidate) in zip(sparse_info_list, sparse_info_candidate)]
    stored_list_list.append(s)

exit((stored_list_list, sparse_info_list))
