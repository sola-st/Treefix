# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Returns the OpDef, Graph and Producer. For use in _apply_op_helper."""
op_def = op_def_registry.get(op_type_name)
if op_def is None:
    raise RuntimeError(f"Unrecognized Op name {op_type_name}")

# Determine the graph context.
try:
    # Need to flatten all the arguments into a list.
    # pylint: disable=protected-access
    g = ops._get_graph_from_inputs(_Flatten(keywords.values()))
    producer = g.graph_def_versions.producer
    # pylint: enable=protected-access
except AssertionError as e:
    raise RuntimeError(
        f"Cannot determine graph for Op '{op_type_name}' due to: {e.message}")

exit((op_def, g, producer))
