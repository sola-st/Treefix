# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
with test_util.use_gpu():
    indices = [
        array_ops.placeholder(dtype=dtypes.int32),
        constant_op.constant(1)
    ]
    data = [constant_op.constant(40), constant_op.constant(60)]
    for step in -1, 1:
        stitched_t = self.stitch_op(indices[::step], data)
        # Dimension 0 is max(flatten(indices))+1, but the first indices input is
        # not a constant tensor, so we can only infer it as a vector of unknown
        # length.
        self.assertEqual([None], stitched_t.get_shape().as_list())
