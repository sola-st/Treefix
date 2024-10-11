# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
# fft_length unused for complex FFTs.
with self.cached_session() as sess:
    exit(sess.run(self._tf_fft_for_rank(rank)(x), feed_dict=feed_dict))
