# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
message = pfor_input.get_attr("message")
exit(wrap(gen_array_ops.check_numerics(t, message), True))
