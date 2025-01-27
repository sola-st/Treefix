# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Disables the V2 dtype behavior for Keras layers.

  See `tf.compat.v1.keras.layers.enable_v2_dtype_behavior`.
  """
global V2_DTYPE_BEHAVIOR
V2_DTYPE_BEHAVIOR = False
