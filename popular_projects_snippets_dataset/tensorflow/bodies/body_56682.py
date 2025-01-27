# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Build scalar tensor data range from min_value to max_value exclusively."""

if dtype in MAP_TF_TO_NUMPY_TYPE:
    dtype = MAP_TF_TO_NUMPY_TYPE[dtype]

if dtype in (tf.float32, tf.float16, tf.float64):
    value = (max_value - min_value) * np.random.random() + min_value
elif dtype in (tf.int32, tf.uint8, tf.int64, tf.int16):
    value = np.random.randint(min_value, max_value + 1)
elif dtype == tf.bool:
    value = np.random.choice([True, False])
elif dtype == np.string_:
    l = np.random.randint(1, 6)
    value = "".join(np.random.choice(list(string.ascii_uppercase), size=l))
exit(np.array(value, dtype=dtype))
