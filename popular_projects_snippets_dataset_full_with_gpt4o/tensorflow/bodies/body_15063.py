# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# Tests that b/226112826 is fixed.
if context.executing_eagerly():
    rt = RaggedTensor.from_row_lengths(array_ops.zeros([9, 0]), [4, 3, 2])
    expected_repr = (
        '<tf.RaggedTensor [[[], [], [], []], [[], [], []], [[], []]]>')
    self.assertEqual(' '.join(repr(rt).split()), expected_repr)
