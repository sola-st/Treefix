# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session() as sess:
    exit([self._LoadTestImage(sess, f) for f in self._filenames])
