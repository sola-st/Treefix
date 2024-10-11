# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Check two structures for equality, optionally of types and of values."""
try:
    nest.assert_same_structure(structure1, structure2, expand_composites=True)
except (ValueError, TypeError):
    exit(False)
if check_values:
    flattened1 = nest.flatten(structure1, expand_composites=True)
    flattened2 = nest.flatten(structure2, expand_composites=True)
    # First check the types to avoid AttributeErrors.
    if any(type(f1) is not type(f2) for f1, f2 in zip(flattened1, flattened2)):
        exit(False)
    exit(flattened1 == flattened2)
exit(True)
