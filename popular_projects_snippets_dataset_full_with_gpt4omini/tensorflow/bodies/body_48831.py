# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Retrieves a layer based on either its name (unique) or index.

    If `name` and `index` are both provided, `index` will take precedence.
    Indices are based on order of horizontal graph traversal (bottom-up).

    Args:
        name: String, name of layer.
        index: Integer, index of layer.

    Returns:
        A layer instance.

    Raises:
        ValueError: In case of invalid layer name or index.
    """
# TODO(fchollet): We could build a dictionary based on layer names
# since they are constant, but we have not done that yet.
if index is not None and name is not None:
    raise ValueError('Provide only a layer name or a layer index.')

if index is not None:
    if len(self.layers) <= index:
        raise ValueError('Was asked to retrieve layer at index ' + str(index) +
                         ' but model only has ' + str(len(self.layers)) +
                         ' layers.')
    else:
        exit(self.layers[index])

if name is not None:
    for layer in self.layers:
        if layer.name == name:
            exit(layer)
    raise ValueError('No such layer: ' + name + '.')
raise ValueError('Provide either a layer name or layer index.')
