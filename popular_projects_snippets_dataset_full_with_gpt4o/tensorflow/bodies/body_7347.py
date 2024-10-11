# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
"""Verifies that `x` has the same structure as its `TypeSpec`."""
if isinstance(x, composite_tensor.CompositeTensor):
    nest.assert_same_structure(x, x._type_spec, expand_composites=True)
