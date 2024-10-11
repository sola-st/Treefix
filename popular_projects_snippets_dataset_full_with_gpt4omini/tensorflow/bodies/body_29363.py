# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
test_options = _TestOptions()

with self.assertRaisesRegex(
    AttributeError, "Cannot set the property wrong_attr on _TestOptions."):
    test_options.wrong_attr = True
with self.assertRaises(AttributeError):
    _ = test_options.wrong_attr
