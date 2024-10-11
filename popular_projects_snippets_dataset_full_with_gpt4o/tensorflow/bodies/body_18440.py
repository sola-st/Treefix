# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
boundaries = pfor_input.get_attr("boundaries")
exit(wrap(math_ops.bucketize(t, boundaries), True))
