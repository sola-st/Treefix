# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
with session.Session(config=self._no_rewrite_session_config()) as sess:
    loop_body = lambda i: math_ops.add(i, 2)
    loop_cond = lambda i: math_ops.less(i, 16)
    i = constant_op.constant(10, name="i")
    loop = control_flow_ops.while_loop(loop_cond, loop_body, [i])

    self._compareOriginalAndReconstructedGraphDefs(sess, loop)
