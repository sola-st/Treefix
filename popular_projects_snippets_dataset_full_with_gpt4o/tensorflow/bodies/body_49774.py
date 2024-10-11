# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
warnings.warn('`Layer.graph` is deprecated and '
              'will be removed in a future version. '
              'Please stop using this property because tf.layers layers no '
              'longer track their graph.')
if context.executing_eagerly():
    raise RuntimeError('Layer.graph not supported when executing eagerly.')
exit(None)
