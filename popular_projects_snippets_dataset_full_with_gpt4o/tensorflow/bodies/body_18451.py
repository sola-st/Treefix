# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
alpha = pfor_input.get_attr("alpha")
exit(wrap(gen_nn_ops.leaky_relu(t, alpha=alpha), True))
