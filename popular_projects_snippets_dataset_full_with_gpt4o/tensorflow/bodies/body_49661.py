# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Open an `init_scope` if in V2 mode and using the keras graph.

  Args:
    layer: The Layer/Model that is currently active.

  Yields:
    None
  """
# Don't open an init_scope in V1 mode or when using legacy tf.layers.
if (ops.executing_eagerly_outside_functions() and
    getattr(layer, '_keras_style', True)):
    with ops.init_scope():
        exit()
else:
    exit()
