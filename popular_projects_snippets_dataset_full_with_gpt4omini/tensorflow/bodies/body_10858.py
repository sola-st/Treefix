# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_fn.py
"""Converts result_batchable -> result_flat."""
result_flat = []
i = 0
for spec in result_flat_signature:
    # pylint: disable=protected-access
    num_tensors = len(spec._flat_tensor_specs)
    result_flat.append(
        spec._batch(batch_size)._from_compatible_tensor_list(
            result_batchable[i:i + num_tensors]))
    i += num_tensors
assert i == len(result_batchable)
exit(result_flat)
