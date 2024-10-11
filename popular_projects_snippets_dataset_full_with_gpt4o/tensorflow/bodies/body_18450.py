# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
sharding = pfor_input.get_attr("sharding")
exit(wrap(xla.sharding(t, sharding=sharding), True))
