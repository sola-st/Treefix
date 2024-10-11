# Extracted from ./data/repos/tensorflow/tensorflow/lite/experimental/microfrontend/python/kernel_tests/audio_microfrontend_op_test.py
with self.test_session():
    audio = tf.constant(
        [0, 32767, 0, -32768] * ((WINDOW_SIZE + 4 * WINDOW_STEP) // 4),
        tf.int16)
    filterbanks = frontend_op.audio_microfrontend(
        audio,
        sample_rate=SAMPLE_RATE,
        window_size=WINDOW_SIZE,
        window_step=WINDOW_STEP,
        num_channels=NUM_CHANNELS,
        upper_band_limit=UPPER_BAND_LIMIT,
        lower_band_limit=LOWER_BAND_LIMIT,
        smoothing_bits=SMOOTHING_BITS,
        enable_pcan=True,
        out_scale=64,
        out_type=tf.float32)
    self.assertAllEqual(
        self.evaluate(filterbanks),
        [[7.484375, 6.640625], [6.8125, 5.90625], [6.40625, 5.46875],
         [6.109375, 5.078125]])
