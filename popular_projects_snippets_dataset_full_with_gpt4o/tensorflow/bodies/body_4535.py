# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/wav_to_features.py
# We want to see all the logging messages.
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
wav_to_features(FLAGS.sample_rate, FLAGS.clip_duration_ms,
                FLAGS.window_size_ms, FLAGS.window_stride_ms,
                FLAGS.feature_bin_count, FLAGS.quantize, FLAGS.preprocess,
                FLAGS.input_wav, FLAGS.output_c_file)
tf.compat.v1.logging.info('Wrote to "%s"' % (FLAGS.output_c_file))
