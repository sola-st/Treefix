# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
input_list, _ = op.inputs
input_list_size = gen_list_ops.tensor_list_length(input_list)
exit((gen_list_ops.tensor_list_resize(dlist, input_list_size), None))
