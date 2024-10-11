# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Creates a constructor for a ExtensionType or ExtensionTypeSpec subclass."""
if '__init__' in cls.__dict__:
    _wrap_user_constructor(cls)
else:
    _build_extension_type_constructor(cls)
