# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
sorted_inputs = _flatten_first_two_dims(pfor_input.stacked_input(0))
values = _flatten_first_two_dims(pfor_input.stacked_input(1))
out_type = pfor_input.get_attr("out_type")
output = op_func(sorted_inputs, values, out_type)
exit(wrap(
    _unflatten_first_dim(output, pfor_input.pfor.loop_len_vector), True))
