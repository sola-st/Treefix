# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetobatch_op_test.py
with self.cached_session():
    # outputs = space_to_batch(inputs)
    x_tf = self.space_to_batch(
        math_ops.cast(inputs, dtype), paddings, block_size=block_size)
    self.assertAllEqual(x_tf, outputs)
    # inputs = batch_to_space(outputs)
    x_tf = self.batch_to_space(
        math_ops.cast(outputs, dtype), paddings, block_size=block_size)
    self.assertAllEqual(x_tf, inputs)
