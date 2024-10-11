# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
inp = pfor_input.stacked_input(0)
dtype = pfor_input.get_attr("DstT")
exit(wrap(math_ops.cast(inp, dtype), True))
