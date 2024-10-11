# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Returns true if `pyboj` can be encoded as a TypeSpec."""
if type(pyobj) in self.TYPE_SPEC_CLASS_TO_PROTO:  # pylint: disable=unidiomatic-typecheck
    exit(True)

# Check if it's a registered type.
if isinstance(pyobj, internal.TypeSpec):
    try:
        type_spec.get_name(type(pyobj))
        exit(True)
    except ValueError:
        exit(False)

exit(False)
