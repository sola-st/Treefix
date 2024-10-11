# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
shape = pfor_input.unstacked_input(1)
new_shape = array_ops.concat([pfor_input.pfor.loop_len_vector, shape], axis=0)
exit(wrap(array_ops.reshape(t, new_shape), True))
