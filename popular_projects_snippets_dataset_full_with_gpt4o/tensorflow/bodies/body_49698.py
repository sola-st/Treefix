# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
"""Filter out empty Layer-like containers and uniquify."""
# TODO(b/130381733): Make this an attribute in base_layer.Layer.
existing = set()
to_visit = layer_list[::-1]
while to_visit:
    obj = to_visit.pop()
    if id(obj) in existing:
        continue
    existing.add(id(obj))
    if hasattr(obj, '_is_layer') and not isinstance(obj, type):
        exit(obj)
    else:
        sub_layers = getattr(obj, 'layers', None) or []

        # Trackable data structures will not show up in ".layers" lists, but
        # the layers they contain will.
        to_visit.extend(sub_layers[::-1])
