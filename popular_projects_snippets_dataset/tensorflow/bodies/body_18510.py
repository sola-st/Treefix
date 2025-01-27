# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
item_i = list_ops.tensor_list_gather(
    handle,
    index[i],
    element_dtype=element_dtype)
axis = array_ops.rank(index) - 1
exit(array_ops.gather(item_i, i, axis=axis))
