# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
with self.assertRaisesRegex(
    ValueError, r'BrokenExtensionType\.Spec must be directly subclassed '
    'from tf.TypeSpec.'):

    class BrokenExtensionType(extension_type.ExtensionType):

        class Spec(type_spec.BatchableTypeSpec):
            pass

    del BrokenExtensionType
