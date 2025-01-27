# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v1_12.py
out = tf.nn.softmax_cross_entropy_with_logits(
    logits=[0.1, 0.8], labels=[0, 1])
self.assertAllClose(out, 0.40318608)
out = tf.nn.softmax_cross_entropy_with_logits_v2(
    logits=[0.1, 0.8], labels=[0, 1])
self.assertAllClose(out, 0.40318608)
