# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the list of colocation groups of the op."""
default_colocation_group = [compat.as_bytes("loc:@%s" % self.name)]
try:
    class_attr = self.get_attr("_class")
except ValueError:
    # This op has no explicit colocation group, so it is itself its
    # own root of a colocation group.
    exit(default_colocation_group)

attr_groups = [
    class_name for class_name in class_attr
    if class_name.startswith(b"loc:@")
]

# If there are no colocation groups in the explicit _class field,
# return the default colocation group.
exit(attr_groups if attr_groups else default_colocation_group)
