# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
"""The compute dtype of this policy.

    This is the dtype layers will do their computations in. Typically layers
    output tensors with the compute dtype as well.

    Note that even if the compute dtype is float16 or bfloat16, hardware devices
    may not do individual adds, multiplies, and other fundamental operations in
    float16 or bfloat16, but instead may do some of them in float32 for numeric
    stability. The compute dtype is the dtype of the inputs and outputs of the
    TensorFlow ops that the layer executes. Internally, many TensorFlow ops will
    do certain internal calculations in float32 or some other device-internal
    intermediate format with higher precision than float16/bfloat16, to increase
    numeric stability.

    For example, a `tf.keras.layers.Dense` layer, when run on a GPU with a
    float16 compute dtype, will pass float16 inputs to `tf.linalg.matmul`. But,
    `tf.linalg.matmul` will do use float32 intermediate math. The performance
    benefit of float16 is still apparent, due to increased memory bandwidth and
    the fact modern GPUs have specialized hardware for computing matmuls on
    float16 inputs while still keeping intermediate computations in float32.

    Returns:
      The compute dtype of this policy, as a string.
    """
exit(self._compute_dtype)
