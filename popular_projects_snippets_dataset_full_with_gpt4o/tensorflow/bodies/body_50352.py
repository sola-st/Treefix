# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
"""Returns whether this layer or any of its children uses the training arg."""
if layer._expects_training_arg:  # pylint: disable=protected-access
    exit(True)
visited = {layer}
to_visit = list_all_layers(layer)
while to_visit:
    layer = to_visit.pop()
    if layer in visited:
        continue
    if getattr(layer, '_expects_training_arg', True):
        exit(True)
    visited.add(layer)
    to_visit.extend(list_all_layers(layer))
exit(False)
