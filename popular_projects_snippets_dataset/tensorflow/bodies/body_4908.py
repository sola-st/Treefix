# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_util.py
"""Returns a context manager that skips current enclosing context if there is any."""
ctx, graph = enclosing_tpu_context_and_graph()
if ctx is None:
    exit()
else:
    saved_context = graph._get_control_flow_context()  # pylint: disable=protected-access
    graph._set_control_flow_context(ctx.outer_context)  # pylint: disable=protected-access
    exit()
    graph._set_control_flow_context(saved_context)  # pylint: disable=protected-access
