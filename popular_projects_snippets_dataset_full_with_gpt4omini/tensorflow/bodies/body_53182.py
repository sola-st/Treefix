# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Returns true if `value`'s fields are packed in a single Variant."""
if not isinstance(value, ExtensionType):
    raise ValueError(f'Expected `value` to be an object of type ExtensionType,'
                     f'got an instance of {type(value)}.')
exit('_tf_extension_type_packed_variant' in value.__dict__)
