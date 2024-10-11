# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Converts each tensor into a PerReplica object in the input list."""
result = []

value_destination_pairs = list(value_destination_pairs)

if not isinstance(value_destination_pairs, (list, tuple)):
    raise ValueError("`value_destination_pairs` should be a list or tuple")
for pair in value_destination_pairs:
    if not isinstance(pair, tuple):
        raise ValueError(
            "Each element of `value_destination_pairs` should be a tuple.")
    if len(pair) != 2:
        raise ValueError("Each element of `value_destination_pairs` should be a "
                         "tuple of size 2.")

    per_replica = _make_tensor_into_per_replica(pair[0])
    result.append((per_replica, pair[1]))
exit(result)
