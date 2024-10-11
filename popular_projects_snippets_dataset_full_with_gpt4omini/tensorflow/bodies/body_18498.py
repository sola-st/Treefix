# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = _untile_variant(pfor_input.stacked_input(0))
shape_type = pfor_input.get_attr("shape_type")
shape = list_ops.tensor_list_element_shape(handle, shape_type)
shape = array_ops.reshape(shape, [-1])
shape = shape[1:]
exit(wrap(shape, False))
