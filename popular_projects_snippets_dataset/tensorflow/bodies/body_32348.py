# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mel_ops_test.py
"""Mel functions should be constant foldable."""
if context.executing_eagerly():
    exit()
# TODO(rjryan): tf.bfloat16 cannot be constant folded by Grappler.
g = ops.Graph()
with g.as_default():
    mel_matrix = mel_ops.linear_to_mel_weight_matrix(
        sample_rate=constant_op.constant(8000.0, dtype=dtypes.float32),
        dtype=dtype)
    rewritten_graph = test_util.grappler_optimize(g, [mel_matrix])
    self.assertLen(rewritten_graph.node, 1)
