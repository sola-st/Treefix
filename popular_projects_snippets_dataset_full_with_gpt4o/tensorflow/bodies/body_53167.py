# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if type(self) is ExtensionType:  # pylint: disable=unidiomatic-typecheck
    raise AssertionError('Cannot create an instance of ExtensionType '
                         'because ExtensionType is an abstract base class.')
