# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
with self.assertRaisesRegex(ValueError, error):
    extension_type.AnonymousExtensionType(**fields)
