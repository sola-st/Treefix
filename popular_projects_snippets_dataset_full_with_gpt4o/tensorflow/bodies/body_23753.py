# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
"""Filter out empty Layer-like containers and uniquify."""
# TODO(b/130381733): Make this an attribute in base_layer.Layer.
existing = object_identity.ObjectIdentitySet()
to_visit = layer_list[::-1]
while to_visit:
    obj = to_visit.pop()
    if obj in existing:
        continue
    existing.add(obj)
    if is_layer(obj):
        exit(obj)
    else:
        sub_layers = getattr(obj, "layers", None) or []

        # Trackable data structures will not show up in ".layers" lists, but
        # the layers they contain will.
        to_visit.extend(sub_layers[::-1])
