# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Builds a TensorFlow graph to apply the input distortions.

    Creates a graph that loads a WAVE file, decodes it, scales the volume,
    shifts it in time, adds in background noise, calculates a spectrogram, and
    then builds an MFCC fingerprint from that.

    This must be called with an active TensorFlow session running, and it
    creates multiple placeholder inputs, and one output:

      - wav_filename_placeholder_: Filename of the WAV to load.
      - foreground_volume_placeholder_: How loud the main clip should be.
      - time_shift_padding_placeholder_: Where to pad the clip.
      - time_shift_offset_placeholder_: How much to move the clip in time.
      - background_data_placeholder_: PCM sample data for background noise.
      - background_volume_placeholder_: Loudness of mixed-in background.
      - output_: Output 2D fingerprint of processed audio.

    Args:
      model_settings: Information about the current model being trained.
      summaries_dir: Path to save training summary information to.

    Raises:
      ValueError: If the preprocessing mode isn't recognized.
      Exception: If the preprocessor wasn't compiled in.
    """
with tf.compat.v1.get_default_graph().name_scope('data'):
    desired_samples = model_settings['desired_samples']
    self.wav_filename_placeholder_ = tf.compat.v1.placeholder(
        tf.string, [], name='wav_filename')
    wav_loader = io_ops.read_file(self.wav_filename_placeholder_)
    wav_decoder = tf.audio.decode_wav(
        wav_loader, desired_channels=1, desired_samples=desired_samples)
    # Allow the audio sample's volume to be adjusted.
    self.foreground_volume_placeholder_ = tf.compat.v1.placeholder(
        tf.float32, [], name='foreground_volume')
    scaled_foreground = tf.multiply(wav_decoder.audio,
                                    self.foreground_volume_placeholder_)
    # Shift the sample's start position, and pad any gaps with zeros.
    self.time_shift_padding_placeholder_ = tf.compat.v1.placeholder(
        tf.int32, [2, 2], name='time_shift_padding')
    self.time_shift_offset_placeholder_ = tf.compat.v1.placeholder(
        tf.int32, [2], name='time_shift_offset')
    padded_foreground = tf.pad(
        tensor=scaled_foreground,
        paddings=self.time_shift_padding_placeholder_,
        mode='CONSTANT')
    sliced_foreground = tf.slice(padded_foreground,
                                 self.time_shift_offset_placeholder_,
                                 [desired_samples, -1])
    # Mix in background noise.
    self.background_data_placeholder_ = tf.compat.v1.placeholder(
        tf.float32, [desired_samples, 1], name='background_data')
    self.background_volume_placeholder_ = tf.compat.v1.placeholder(
        tf.float32, [], name='background_volume')
    background_mul = tf.multiply(self.background_data_placeholder_,
                                 self.background_volume_placeholder_)
    background_add = tf.add(background_mul, sliced_foreground)
    background_clamp = tf.clip_by_value(background_add, -1.0, 1.0)
    # Run the spectrogram and MFCC ops to get a 2D 'fingerprint' of the audio.
    spectrogram = audio_ops.audio_spectrogram(
        background_clamp,
        window_size=model_settings['window_size_samples'],
        stride=model_settings['window_stride_samples'],
        magnitude_squared=True)
    tf.compat.v1.summary.image(
        'spectrogram', tf.expand_dims(spectrogram, -1), max_outputs=1)
    # The number of buckets in each FFT row in the spectrogram will depend on
    # how many input samples there are in each window. This can be quite
    # large, with a 160 sample window producing 127 buckets for example. We
    # don't need this level of detail for classification, so we often want to
    # shrink them down to produce a smaller result. That's what this section
    # implements. One method is to use average pooling to merge adjacent
    # buckets, but a more sophisticated approach is to apply the MFCC
    # algorithm to shrink the representation.
    if model_settings['preprocess'] == 'average':
        self.output_ = tf.nn.pool(
            input=tf.expand_dims(spectrogram, -1),
            window_shape=[1, model_settings['average_window_width']],
            strides=[1, model_settings['average_window_width']],
            pooling_type='AVG',
            padding='SAME')
        tf.compat.v1.summary.image('shrunk_spectrogram',
                                   self.output_,
                                   max_outputs=1)
    elif model_settings['preprocess'] == 'mfcc':
        self.output_ = audio_ops.mfcc(
            spectrogram,
            wav_decoder.sample_rate,
            dct_coefficient_count=model_settings['fingerprint_width'])
        tf.compat.v1.summary.image(
            'mfcc', tf.expand_dims(self.output_, -1), max_outputs=1)
    elif model_settings['preprocess'] == 'micro':
        if not frontend_op:
            raise Exception(
                'Micro frontend op is currently not available when running'
                ' TensorFlow directly from Python, you need to build and run'
                ' through Bazel')
        sample_rate = model_settings['sample_rate']
        window_size_ms = (model_settings['window_size_samples'] *
                          1000) / sample_rate
        window_step_ms = (model_settings['window_stride_samples'] *
                          1000) / sample_rate
        int16_input = tf.cast(tf.multiply(background_clamp, 32768), tf.int16)
        micro_frontend = frontend_op.audio_microfrontend(
            int16_input,
            sample_rate=sample_rate,
            window_size=window_size_ms,
            window_step=window_step_ms,
            num_channels=model_settings['fingerprint_width'],
            out_scale=1,
            out_type=tf.float32)
        self.output_ = tf.multiply(micro_frontend, (10.0 / 256.0))
        tf.compat.v1.summary.image(
            'micro',
            tf.expand_dims(tf.expand_dims(self.output_, -1), 0),
            max_outputs=1)
    else:
        raise ValueError('Unknown preprocess mode "%s" (should be "mfcc", '
                         ' "average", or "micro")' %
                         (model_settings['preprocess']))

    # Merge all the summaries and write them out to /tmp/retrain_logs (by
    # default)
    self.merged_summaries_ = tf.compat.v1.summary.merge_all(scope='data')
    if summaries_dir:
        self.summary_writer_ = tf.compat.v1.summary.FileWriter(
            summaries_dir + '/data', tf.compat.v1.get_default_graph())
