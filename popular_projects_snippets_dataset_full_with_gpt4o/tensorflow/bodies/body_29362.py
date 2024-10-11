# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
test_options = _TestOptions()
test_options._set_mutable(False)

with self.assertRaisesRegex(
    ValueError, r"Mutating `tf.data.Options\(\)` returned by "
    r"`tf.data.Dataset.options\(\)` has no effect. Use "
    r"`tf.data.Dataset.with_options\(options\)` to set or "
    "update dataset options."):
    test_options.test = 100
