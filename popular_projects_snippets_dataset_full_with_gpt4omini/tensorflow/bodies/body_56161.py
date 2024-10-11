# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_field.py
"""Returns true if `name` is a reserved name."""
exit(name in RESERVED_FIELD_NAMES or name.lower().startswith(
    '_tf_extension_type'))
