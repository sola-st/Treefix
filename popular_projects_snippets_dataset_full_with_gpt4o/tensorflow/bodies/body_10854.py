# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""Converts result_flat_signature -> result_batchable_tensor_specs."""
tensor_specs = []
for spec in result_flat_signature:
    if not isinstance(spec, type_spec.BatchableTypeSpec):
        raise TypeError("map_fn can not generate %s outputs" % (spec,))
    tensor_specs.extend(spec._flat_tensor_specs)  # pylint: disable=protected-access
exit(tensor_specs)
