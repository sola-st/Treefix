# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
exit(any(name == field.name for field in cls._tf_extension_type_fields()))
