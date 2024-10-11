# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if not self.symbol:
    raise ValueError('This Keras op layer was generated from %s, a method '
                     'that is not an exposed in the TensorFlow API. This '
                     'may have happened if the method was explicitly '
                     'decorated to add dispatching support, and it was used '
                     'during Functional model construction. '
                     'To ensure cross-version compatibility of Keras models '
                     'that use op layers, only op layers produced from '
                     'exported TF API symbols can be serialized.'
                     % self.function)
config = {
    'function': self.symbol
}

base_config = super(TFOpLambda, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
