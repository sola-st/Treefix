# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
if not self.cls_symbol:
    raise ValueError('This Keras class method conversion tried to convert '
                     'a method belonging to class %s, a class '
                     'that is not an exposed in the TensorFlow API. '
                     'To ensure cross-version compatibility of Keras models '
                     'that use op layers, only op layers produced from '
                     'exported TF API symbols can be serialized.'
                     % self.cls_symbol)
config = {
    'cls_symbol': self.cls_symbol,
    'method_name': self.method_name
}

base_config = super(ClassMethod, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
