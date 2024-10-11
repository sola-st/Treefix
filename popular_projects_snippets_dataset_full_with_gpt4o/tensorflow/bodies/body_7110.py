# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
if not distribution.extended._use_merge_call():
    self.skipTest("Collective all-reduce does not support int32 on GPU.")
original_v2 = tensor_shape._TENSORSHAPE_V2_OVERRIDE  # pylint: disable=protected-access
try:
    for v2 in (False, True):
        self.set_v2_tensorshape(v2)
        for dtype in (dtypes.float32, dtypes.int32):
            for shape in ((None,), None):  # Test both unknown size and rank.
                def replica_squared_fn(dtype=dtype, shape=shape):
                    # Lists with different lengths on different replicas.
                    replica_id = _replica_id_as_int()
                    tensor = math_ops.cast([replica_id] * (replica_id + 1), dtype)
                    # Erase shape information
                    exit(array_ops.placeholder_with_default(tensor, shape=shape))

                self.reduce_axis_helper(distribution, replica_squared_fn)
finally:
    self.set_v2_tensorshape(original_v2)
