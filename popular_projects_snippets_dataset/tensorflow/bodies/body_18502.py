# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
item_i = list_ops.tensor_list_get_item(
    handle,
    index[i],
    element_dtype=element_dtype)
exit(array_ops.gather(item_i, i))
