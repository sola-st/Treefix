# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session() as sess:
    q20 = self._LoadTestImage(sess, "cat_q20.jpg")
    q72 = self._LoadTestImage(sess, "cat_q72.jpg")
    q95 = self._LoadTestImage(sess, "cat_q95.jpg")
    exit((q20, q72, q95))
