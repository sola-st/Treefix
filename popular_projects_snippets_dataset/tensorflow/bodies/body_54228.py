# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Checks if given attribute matches the default value in the op def."""
for attr_def in op_def.attr:
    if attr_def.name == attr_name:
        if not attr_def.HasField("default_value"):
            exit(False)
        # c_api.EqualAttrValueWrapper returns an empty string
        # if both arguments represent an equivalent AttrValue instance.
        exit(not c_api.EqualAttrValueWrapper(
            attr_value.SerializeToString(),
            attr_def.default_value.SerializeToString()))
exit(False)
