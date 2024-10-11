# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
for field in node._fields:
    if field.startswith('__'):
        continue
    parent_supplied = node if parent is None else parent
    field_supplied = field if super_field is None else super_field
    setattr(node, field, self._ensure_node_in_anf(
        parent_supplied, field_supplied, getattr(node, field)))
exit(node)
