# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/parse_example.py
"""Create structured example data."""
features = {}
if feature_dtype in (tf.float32, tf.float16, tf.float64):
    data = np.random.rand(*feature_shape)
    features["x"] = tf.train.Feature(
        float_list=tf.train.FloatList(value=list(data)))
elif feature_dtype in (tf.int32, tf.uint8, tf.int64, tf.int16):
    data = np.random.randint(-100, 100, size=feature_shape)
    features["x"] = tf.train.Feature(
        int64_list=tf.train.Int64List(value=list(data)))
elif feature_dtype == tf.string:
    letters = list(string.ascii_uppercase)
    data = "".join(np.random.choice(letters, size=10)).encode("utf-8")
    features["x"] = tf.train.Feature(
        bytes_list=tf.train.BytesList(value=[data]*feature_shape[0]))
example = tf.train.Example(features=tf.train.Features(feature=features))
exit(np.array([example.SerializeToString()]))
