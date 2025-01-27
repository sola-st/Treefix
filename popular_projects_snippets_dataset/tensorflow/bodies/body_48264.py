# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
if not hasattr(self, '_originally_built_as_v1'):
    raise ValueError(
        'Your Layer or Model is in an invalid state. '
        'This can happen for the following cases:\n '
        '1. You might be interleaving estimator/non-estimator models or '
        'interleaving models/layers made in tf.compat.v1.Graph.as_default() '
        'with models/layers created outside of it. '
        'Converting a model to an estimator (via model_to_estimator) '
        'invalidates all models/layers made before the conversion (even '
        'if they were not the model converted to an estimator). '
        'Similarly, making a layer or a model inside a '
        'a tf.compat.v1.Graph invalidates all layers/models you previously '
        'made outside of the graph.\n'
        '2. You might be using a custom keras layer implementation with '
        ' custom __init__ which didn\'t call super().__init__. '
        ' Please check the implementation of %s and its bases.' %
        (type(self),))
