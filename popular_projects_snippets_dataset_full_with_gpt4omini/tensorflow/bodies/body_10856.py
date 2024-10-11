# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""Converts elems_value_batchable -> elems_value_flat."""
elems_value_flat = []
i = 0
for spec in elems_flat_signature:
    # pylint: disable=protected-access
    spec = spec._unbatch()
    tensor_list = elems_value_batchable[i:i + len(spec._flat_tensor_specs)]
    elems_value_flat.append(spec._from_compatible_tensor_list(tensor_list))
    i += len(tensor_list)
assert i == len(elems_value_batchable)
exit(elems_value_flat)
