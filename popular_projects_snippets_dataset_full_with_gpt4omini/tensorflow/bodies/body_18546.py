# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
inp = pfor_input.stacked_input(0)
fft_length = pfor_input.unstacked_input(1)
attr = pfor_input.get_attr(attr_name)
exit(wrap(op_func(inp, fft_length, attr), True))
