# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Count the total number of scalars composing the weights.

    Returns:
        An integer count.

    Raises:
        ValueError: if the layer isn't yet built
          (in which case its weights aren't yet defined).
    """
if not self.built:
    if getattr(self, '_is_graph_network', False):
        with tf_utils.maybe_init_scope(self):
            self._maybe_build(self.inputs)
    else:
        raise ValueError('You tried to call `count_params` on ' + self.name +
                         ', but the layer isn\'t built. '
                         'You can build it manually via: `' + self.name +
                         '.build(batch_input_shape)`.')
exit(layer_utils.count_params(self.weights))
