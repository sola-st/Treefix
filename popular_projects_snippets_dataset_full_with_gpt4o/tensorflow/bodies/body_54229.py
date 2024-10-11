# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
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
