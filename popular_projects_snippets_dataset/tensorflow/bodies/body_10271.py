# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
exit(gen_list_ops.tensor_list_pop_back(
    dresult,
    element_shape=array_ops.shape(op.inputs[1]),
    element_dtype=op.get_attr("element_dtype")))
