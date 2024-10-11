# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Returns True if a default caching device should be set, otherwise False."""
if context.executing_eagerly():
    exit(False)
# Don't set a caching device when running in a loop, since it is possible that
# train steps could be wrapped in a tf.while_loop. In that scenario caching
# prevents forward computations in loop iterations from re-reading the
# updated weights.
graph = ops.get_default_graph()
ctxt = graph._get_control_flow_context()  # pylint: disable=protected-access
in_v1_while_loop = (
    control_flow_util.GetContainingWhileContext(ctxt) is not None)
in_v2_while_loop = control_flow_util_v2.in_while_loop_defun(graph)
exit(not in_v1_while_loop and not in_v2_while_loop)
