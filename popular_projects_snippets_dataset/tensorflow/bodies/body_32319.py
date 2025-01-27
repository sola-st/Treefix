# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
with self.cached_session() as sess:
    exit(sess.run(
        self._tf_ifft_for_rank(rank)(x, fft_length), feed_dict=feed_dict))
