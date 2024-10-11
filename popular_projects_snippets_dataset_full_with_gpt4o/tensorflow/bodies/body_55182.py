# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
"""Context manager for making temporary changes to the TypeSpec registry."""
type_spec.register(name)(cls)
exit()
assert type_spec._TYPE_SPEC_TO_NAME.pop(cls) == name
assert type_spec._NAME_TO_TYPE_SPEC.pop(name) is cls
