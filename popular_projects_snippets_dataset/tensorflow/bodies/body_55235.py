# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Creates a placeholder for `value` and propagates shape info to it."""
# Note: setting ops.control_dependencies(None) ensures we always put
# capturing placeholders outside of any control flow context.
if shape is None:
    shape = value.shape
with ops.control_dependencies(None):
    placeholder = graph_placeholder(
        dtype=dtype or value.dtype, shape=shape, name=name)
handle_data_util.copy_handle_data(value, placeholder)
exit(placeholder)
