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
        left_context=1,
        right_context=1)
    self.assertAllEqual(
        self.evaluate(filterbanks),
        [[479, 425, 479, 425, 436, 378], [479, 425, 436, 378, 410, 350],
         [436, 378, 410, 350, 391, 325], [410, 350, 391, 325, 391, 325]])
