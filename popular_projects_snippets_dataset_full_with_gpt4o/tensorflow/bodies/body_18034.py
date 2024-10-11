# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    exit(control_flow_ops.Assert(i < 10, [i, [10], [i + 1]]))

# TODO(agarwal): make this work with for_loop.
with session.Session() as sess:
    sess.run(pfor_control_flow_ops.pfor(loop_fn, 3))
    sess.run(pfor_control_flow_ops.pfor(
        lambda i, pfor_config: loop_fn(i), 3))
