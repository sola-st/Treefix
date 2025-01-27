# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
msg = "Can't instantiate.*abstract"
with self.assertRaisesRegex(TypeError, msg):
    AbstractModule()  # pylint: disable=abstract-class-instantiated
