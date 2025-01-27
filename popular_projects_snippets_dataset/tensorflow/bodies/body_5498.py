# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
values = [_make_indexed_slices(values, indices, dense_shape, d)
          for d in devices]
exit(distribute_utils.regroup(
    values,
    wrap_class=value_lib.Mirrored))
