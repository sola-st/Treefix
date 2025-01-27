# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
paddings = pfor_input.unstacked_input(1)
paddings = array_ops.concat([[[0, 0]], paddings], 0)
exit(wrap(array_ops.pad_v2(t, paddings, mode="CONSTANT"), True))
