# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
block_shape = np.array(block_shape)
paddings = np.array(paddings).reshape((len(block_shape), 2))
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu):
        # outputs = space_to_batch(inputs)
        x_tf = array_ops.space_to_batch_nd(
            math_ops.cast(inputs, dtypes.float32), block_shape, paddings)
        self.assertAllEqual(x_tf, outputs)
        # inputs = batch_to_space(outputs)
        x_tf = array_ops.batch_to_space_nd(
            math_ops.cast(outputs, dtypes.float32), block_shape, paddings)
        self.assertAllEqual(x_tf, inputs)
