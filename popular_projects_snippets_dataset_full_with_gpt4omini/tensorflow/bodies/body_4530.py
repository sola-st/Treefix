# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/freeze.py
"""Creates an audio model with the nodes needed for inference.

  Uses the supplied arguments to create a model, and inserts the input and
  output nodes that are needed to use the graph for inference.

  Args:
    wanted_words: Comma-separated list of the words we're trying to recognize.
    sample_rate: How many samples per second are in the input audio files.
    clip_duration_ms: How many samples to analyze for the audio pattern.
    clip_stride_ms: How often to run recognition. Useful for models with cache.
    window_size_ms: Time slice duration to estimate frequencies from.
    window_stride_ms: How far apart time slices should be.
    feature_bin_count: Number of frequency bands to analyze.
    model_architecture: Name of the kind of model to generate.
    preprocess: How the spectrogram is processed to produce features, for
      example 'mfcc', 'average', or 'micro'.

  Returns:
    Input and output tensor objects.

  Raises:
    Exception: If the preprocessing mode isn't recognized.
  """

words_list = input_data.prepare_words_list(wanted_words.split(','))
model_settings = models.prepare_model_settings(
    len(words_list), sample_rate, clip_duration_ms, window_size_ms,
    window_stride_ms, feature_bin_count, preprocess)
runtime_settings = {'clip_stride_ms': clip_stride_ms}

wav_data_placeholder = tf.compat.v1.placeholder(tf.string, [],
                                                name='wav_data')
decoded_sample_data = tf.audio.decode_wav(
    wav_data_placeholder,
    desired_channels=1,
    desired_samples=model_settings['desired_samples'],
    name='decoded_sample_data')
spectrogram = audio_ops.audio_spectrogram(
    decoded_sample_data.audio,
    window_size=model_settings['window_size_samples'],
    stride=model_settings['window_stride_samples'],
    magnitude_squared=True)

if preprocess == 'average':
    fingerprint_input = tf.nn.pool(
        input=tf.expand_dims(spectrogram, -1),
        window_shape=[1, model_settings['average_window_width']],
        strides=[1, model_settings['average_window_width']],
        pooling_type='AVG',
        padding='SAME')
elif preprocess == 'mfcc':
    fingerprint_input = audio_ops.mfcc(
        spectrogram,
        sample_rate,
        dct_coefficient_count=model_settings['fingerprint_width'])
elif preprocess == 'micro':
    if not frontend_op:
        raise Exception(
            'Micro frontend op is currently not available when running TensorFlow'
            ' directly from Python, you need to build and run through Bazel, for'
            ' example'
            ' `bazel run tensorflow/examples/speech_commands:freeze_graph`')
    sample_rate = model_settings['sample_rate']
    window_size_ms = (model_settings['window_size_samples'] *
                      1000) / sample_rate
    window_step_ms = (model_settings['window_stride_samples'] *
                      1000) / sample_rate
    int16_input = tf.cast(
        tf.multiply(decoded_sample_data.audio, 32767), tf.int16)
    micro_frontend = frontend_op.audio_microfrontend(
        int16_input,
        sample_rate=sample_rate,
        window_size=window_size_ms,
        window_step=window_step_ms,
        num_channels=model_settings['fingerprint_width'],
        out_scale=1,
        out_type=tf.float32)
    fingerprint_input = tf.multiply(micro_frontend, (10.0 / 256.0))
else:
    raise Exception('Unknown preprocess mode "%s" (should be "mfcc",'
                    ' "average", or "micro")' % (preprocess))

fingerprint_size = model_settings['fingerprint_size']
reshaped_input = tf.reshape(fingerprint_input, [-1, fingerprint_size])

logits = models.create_model(
    reshaped_input, model_settings, model_architecture, is_training=False,
    runtime_settings=runtime_settings)

# Create an output to use for inference.
softmax = tf.nn.softmax(logits, name='labels_softmax')

exit((reshaped_input, softmax))
