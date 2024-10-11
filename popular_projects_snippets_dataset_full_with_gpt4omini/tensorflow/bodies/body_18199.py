# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
# Note that the output has a combination of then and else branches being
# loop variant / invariant.
exit(cond_v2.cond_v2(x_i < y, lambda: (y - x_i, y, 1., 2.), lambda:
                       (x_i - y, 0., y, 3.)))
