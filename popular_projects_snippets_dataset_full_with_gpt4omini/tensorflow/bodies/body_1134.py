# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/fft_test.py
for indims in inner_dims:
    print("nfft =", indims)
    shape = BATCH_DIMS + indims
    data = np.arange(np.prod(shape) * 2) / np.prod(indims)
    np.random.seed(123)
    np.random.shuffle(data)
    data = np.reshape(data.astype(np.float32).view(np.complex64), shape)
    data = to_32bit(complex_to_input(data))
    expected = to_32bit(input_to_expected(data))
    with self.session() as sess:
        with self.test_scope():
            ph = array_ops.placeholder(
                dtypes.as_dtype(data.dtype), shape=data.shape)
            out = tf_method(ph)
        value = sess.run(out, {ph: data})
        self.assertAllClose(expected, value, rtol=rtol, atol=atol)
