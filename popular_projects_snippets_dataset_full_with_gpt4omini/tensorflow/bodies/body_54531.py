# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Set any default attr values in `node_def` that aren't present."""
assert node_def.op == op_def.name
for attr_def in op_def.attr:
    key = attr_def.name
    if attr_def.HasField('default_value'):
        value = node_def.attr[key]
        if value is None or value.WhichOneof('value') is None:
            node_def.attr[key].CopyFrom(attr_def.default_value)
