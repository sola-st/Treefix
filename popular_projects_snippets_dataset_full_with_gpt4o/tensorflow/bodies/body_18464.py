# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.expanddim_inputs_for_broadcast()
cond = pfor_input.input(0)[0]
t = pfor_input.input(1)[0]
e = pfor_input.input(2)[0]
out = array_ops.where_v2(cond, t, e)
exit(wrap(out, True))
