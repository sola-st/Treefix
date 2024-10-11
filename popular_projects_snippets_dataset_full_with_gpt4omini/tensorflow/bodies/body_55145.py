# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
with self.assertRaisesRegex(AssertionError,
                            'ExtensionType is an abstract base class.'):
    extension_type.ExtensionType()
