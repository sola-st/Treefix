# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Enable the V2 dtype behavior for Keras layers.

  By default, the V2 dtype behavior is enabled in TensorFlow 2, so this function
  is only useful if `tf.compat.v1.disable_v2_behavior` has been called. Since
  mixed precision requires V2 dtype behavior to be enabled, this function allows
  you to use mixed precision in Keras layers if `disable_v2_behavior` has been
  called.

  When enabled, the dtype of Keras layers defaults to floatx (which is typically
  float32) instead of None. In addition, layers will automatically cast
  floating-point inputs to the layer's dtype.

  >>> x = tf.ones((4, 4, 4, 4), dtype='float64')
  >>> layer = tf.keras.layers.Conv2D(filters=4, kernel_size=2)
  >>> print(layer.dtype)  # float32 since V2 dtype behavior is enabled
  float32
  >>> y = layer(x)  # Layer casts inputs since V2 dtype behavior is enabled
  >>> print(y.dtype.name)
  float32

  A layer author can opt-out their layer from the automatic input casting by
  passing `autocast=False` to the base Layer's constructor. This disables the
  autocasting part of the V2 behavior for that layer, but not the defaulting to
  floatx part of the V2 behavior.

  When a global `tf.keras.mixed_precision.Policy` is set, a Keras layer's dtype
  will default to the global policy instead of floatx. Layers will automatically
  cast inputs to the policy's compute_dtype.
  """
global V2_DTYPE_BEHAVIOR
V2_DTYPE_BEHAVIOR = True
