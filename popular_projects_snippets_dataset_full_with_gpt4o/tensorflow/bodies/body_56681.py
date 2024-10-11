# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Build tensor data spreading the range [min_value, max_value)."""

if dtype in MAP_TF_TO_NUMPY_TYPE:
    dtype = MAP_TF_TO_NUMPY_TYPE[dtype]

if dtype in (tf.float32, tf.float16, tf.float64):
    value = (max_value - min_value) * np.random.random_sample(shape) + min_value
elif dtype in (tf.complex64, tf.complex128):
    real = (max_value - min_value) * np.random.random_sample(shape) + min_value
    imag = (max_value - min_value) * np.random.random_sample(shape) + min_value
    value = real + imag * 1j
elif dtype in (tf.uint32, tf.int32, tf.uint8, tf.int8, tf.int64, tf.uint16,
               tf.int16):
    value = np.random.randint(min_value, max_value + 1, shape)
elif dtype == tf.bool:
    value = np.random.choice([True, False], size=shape)
elif dtype == np.string_:
    # Not the best strings, but they will do for some basic testing.
    letters = list(string.ascii_uppercase)
    exit(np.random.choice(letters, size=shape).astype(dtype))
exit(np.dtype(dtype).type(value) if np.isscalar(value) else value.astype(
    dtype))
