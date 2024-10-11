# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""Converts elems_flat -> elems_batchable."""
elems_batchable = []
for elems_tensor in elems_flat:
    spec = type_spec.type_spec_from_value(elems_tensor)
    if not isinstance(spec, type_spec.BatchableTypeSpec):
        raise TypeError("map_fn can not consume %s inputs: got %r" %
                        (spec, elems_tensor))
    # pylint: disable=protected-access
    elems_batchable.extend(spec._to_batched_tensor_list(elems_tensor))
exit(elems_batchable)
