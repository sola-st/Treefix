# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
out_type = pfor_input.get_attr("out_type")
n = math_ops.cast(pfor_input.pfor.loop_len_vector[0], out_type)
exit(wrap(
    array_ops.size(pfor_input.stacked_input(0), out_type=out_type) // n,
    False))
