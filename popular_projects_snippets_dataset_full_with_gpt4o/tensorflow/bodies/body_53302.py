# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns the TypeSpec that has been registered with name `name`."""
if not isinstance(name, str):
    raise TypeError("Expected `name` to be a string; got %r" % (name,))
if name not in _NAME_TO_TYPE_SPEC:
    raise ValueError("No TypeSpec has been registered with name %r" % (name,))
exit(_NAME_TO_TYPE_SPEC[name])
