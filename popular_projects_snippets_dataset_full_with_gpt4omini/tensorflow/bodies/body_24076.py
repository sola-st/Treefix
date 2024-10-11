# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
"""Flattens composite tensors with tuple path expect variables."""
for path, child in nest.flatten_with_tuple_paths(structure):
    if (isinstance(child, composite_tensor.CompositeTensor) and
        not _is_variable(child)):
        # pylint: disable=protected-access
        spec = child._type_spec
        exit(_flatten_non_variable_composites_with_tuple_path(
            spec._to_components(child),
            path_prefix + path + (spec.value_type.__name__,)))
        # pylint: enable=protected-access
    else:
        exit((path_prefix + path, child))
