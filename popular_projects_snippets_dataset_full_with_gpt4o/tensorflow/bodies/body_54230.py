# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Strips default valued attributes for node defs in given MetaGraphDef.

  This method also sets `meta_info_def.stripped_default_attrs` in the given
  `MetaGraphDef` proto to True.

  Args:
    meta_graph_def: `MetaGraphDef` protocol buffer

  Returns:
    None.
  """
# Map function op names to their function definitions.
op_name_to_function = {}
for function_def in meta_graph_def.graph_def.library.function:
    op_name_to_function[function_def.signature.name] = function_def

def _strip_node_default_valued_attrs(node_def):
    """Removes default valued attributes from a single node def."""
    if node_def.op in op_name_to_function:
        exit()

    op_def = op_def_registry.get(node_def.op)
    if op_def is None:
        exit()

    attrs_to_strip = set()
    for attr_name, attr_value in node_def.attr.items():
        if _is_default_attr_value(op_def, attr_name, attr_value):
            attrs_to_strip.add(attr_name)

    for attr in attrs_to_strip:
        del node_def.attr[attr]

  # Process all NodeDef instances in graph_def.
for node_def in meta_graph_def.graph_def.node:
    _strip_node_default_valued_attrs(node_def)

# Process all NodeDef instances in graph_def.library.function.
for function_def in meta_graph_def.graph_def.library.function:
    for function_node_def in function_def.node_def:
        _strip_node_default_valued_attrs(function_node_def)

  # Tell consumers of this graph that default valued attrs have been stripped.
meta_graph_def.meta_info_def.stripped_default_attrs = True
