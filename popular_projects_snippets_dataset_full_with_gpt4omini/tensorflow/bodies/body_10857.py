# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""Converts result_value_flat -> result_value_batchable."""
result_value_batchable = []
for (r_value, r_spec) in zip(result_value_flat, result_flat_signature):
    if isinstance(r_spec, tensor_spec.TensorSpec):
        result_value_batchable.append(r_value)
    else:
        if not r_spec.is_compatible_with(r_value):
            raise ValueError(
                "Error in map_fn:\n  Expected `fn` to return a:\n    %s\n"
                "  But it returned a:\n    %s\n    (value=%s)\n"
                "  To fix, update the `fn_output_signature` (or `dtype`) "
                "argument to `map_fn`." %
                (r_spec, type_spec.type_spec_from_value(r_value), r_value))
        result_value_batchable.extend(r_spec._to_tensor_list(r_value))  # pylint: disable=protected-access
exit(result_value_batchable)
