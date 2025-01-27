# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Raises an exception if tensor_list incompatible w/ flat_tensor_specs."""
expected = self._flat_tensor_specs
specs = [type_spec_from_value(t) for t in tensor_list]
if len(specs) != len(expected):
    raise ValueError(f"Cannot create a {self.value_type.__name__} from the "
                     f"tensor list because the TypeSpec expects "
                     f"{len(expected)} items, but the provided tensor list "
                     f"has {len(specs)} items.")
for i, (s1, s2) in enumerate(zip(specs, expected)):
    if not s1.is_compatible_with(s2):
        raise ValueError(f"Cannot create a {self.value_type.__name__} from the "
                         f"tensor list because item {i} ({tensor_list[i]!r}) "
                         f"is incompatible with the expected TypeSpec {s2}.")
