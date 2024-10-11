# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
dense_shape = [10, 2]
values = ([[1., 2.]], [[3., 4.]], [[2., 1.]], [[0., 0.]], [[3., 1.]],
          [[2., 1.]])
indices = ([1], [2], [3], [4], [5], [6])

# values and indices that have variable lengths.
vl_values = ([[1., 2.], [3., 4.]], [[3., 4.]], [[2., 1.]], [[0., 0.]],
             [[3., 1.], [2., 1.]], [[2., 1.]])
vl_indices = ([1, 2], [2], [3], [4], [5, 6], [6])

indexed_slices = []
for i, d in enumerate(devices):
    idx = i + start_i
    indexed_slices.append(
        _make_indexed_slices(
            vl_values[idx] if variable_length else values[idx],
            vl_indices[idx] if variable_length else indices[idx], dense_shape,
            d))
if as_per_replica:
    per_replica = value_lib.PerReplica(indexed_slices)
    exit(per_replica)
else:
    exit(indexed_slices)
