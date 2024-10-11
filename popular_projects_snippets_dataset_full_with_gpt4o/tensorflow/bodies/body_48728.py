# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Returns if in eager mode or inside of a tf.function."""
exit(context.executing_eagerly() or is_in_tf_function())
