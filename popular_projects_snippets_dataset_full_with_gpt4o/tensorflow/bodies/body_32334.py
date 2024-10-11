# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/fft_ops_test.py
# TODO(rjryan): Fix this test under Eager.
if context.executing_eagerly():
    exit()
for rank in VALID_FFT_RANKS:
    for dims in range(0, rank):
        x = np.zeros((1,) * dims).astype(np.complex64)
        with self.assertRaisesWithPredicateMatch(
            ValueError, "Shape .* must have rank at least {}".format(rank)):
            self._tf_fft(x, rank)
        with self.assertRaisesWithPredicateMatch(
            ValueError, "Shape .* must have rank at least {}".format(rank)):
            self._tf_ifft(x, rank)
    for dims in range(rank, rank + 2):
        x = np.zeros((1,) * rank)

        # Test non-rank-1 fft_length produces an error.
        fft_length = np.zeros((1, 1)).astype(np.int32)
        with self.assertRaisesWithPredicateMatch(ValueError,
                                                 "Shape .* must have rank 1"):
            self._tf_fft(x, rank, fft_length)
        with self.assertRaisesWithPredicateMatch(ValueError,
                                                 "Shape .* must have rank 1"):
            self._tf_ifft(x, rank, fft_length)

        # Test wrong fft_length length.
        fft_length = np.zeros((rank + 1,)).astype(np.int32)
        with self.assertRaisesWithPredicateMatch(
            ValueError, "Dimension must be .*but is {}.*".format(rank + 1)):
            self._tf_fft(x, rank, fft_length)
        with self.assertRaisesWithPredicateMatch(
            ValueError, "Dimension must be .*but is {}.*".format(rank + 1)):
            self._tf_ifft(x, rank, fft_length)

      # Test that calling the kernel directly without padding to fft_length
      # produces an error.
    rffts_for_rank = {
        1: [gen_spectral_ops.rfft, gen_spectral_ops.irfft],
        2: [gen_spectral_ops.rfft2d, gen_spectral_ops.irfft2d],
        3: [gen_spectral_ops.rfft3d, gen_spectral_ops.irfft3d]
    }
    rfft_fn, irfft_fn = rffts_for_rank[rank]
    with self.assertRaisesWithPredicateMatch(
        errors.InvalidArgumentError,
        "Input dimension .* must have length of at least 6 but got: 5"):
        x = np.zeros((5,) * rank).astype(np.float32)
        fft_length = [6] * rank
        with self.cached_session():
            self.evaluate(rfft_fn(x, fft_length))

    with self.assertRaisesWithPredicateMatch(
        errors.InvalidArgumentError,
        "Input dimension .* must have length of at least .* but got: 3"):
        x = np.zeros((3,) * rank).astype(np.complex64)
        fft_length = [6] * rank
        with self.cached_session():
            self.evaluate(irfft_fn(x, fft_length))
