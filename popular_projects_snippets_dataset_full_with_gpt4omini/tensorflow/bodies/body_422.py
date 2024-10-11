# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
# TODO(aselle): Test sparse_softmax_...
with self.cached_session():
    labels = [.8, .5, .2, .1]
    logits = [.9, .1, .3, .1]
    self.assertAllEqual(
        tf.nn.softmax_cross_entropy_with_logits(
            logits, labels).eval(),
        tf.nn.softmax_cross_entropy_with_logits(
            labels=labels, logits=logits).eval())
    self.assertAllEqual(
        tf.nn.sigmoid_cross_entropy_with_logits(
            logits, labels).eval(),
        tf.nn.sigmoid_cross_entropy_with_logits(
            labels=labels, logits=logits).eval())
