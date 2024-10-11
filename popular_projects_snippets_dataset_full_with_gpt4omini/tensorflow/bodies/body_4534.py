# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/wav_to_features.py
"""Converts an audio file into its corresponding feature map.

  Args:
    sample_rate: Expected sample rate of the wavs.
    clip_duration_ms: Expected duration in milliseconds of the wavs.
    window_size_ms: How long each spectrogram timeslice is.
    window_stride_ms: How far to move in time between spectrogram timeslices.
    feature_bin_count: How many bins to use for the feature fingerprint.
    quantize: Whether to train the model for eight-bit deployment.
    preprocess: Spectrogram processing mode; "mfcc", "average" or "micro".
    input_wav: Path to the audio WAV file to read.
    output_c_file: Where to save the generated C source file.
  """

# Start a new TensorFlow session.
sess = tf.compat.v1.InteractiveSession()

model_settings = models.prepare_model_settings(
    0, sample_rate, clip_duration_ms, window_size_ms, window_stride_ms,
    feature_bin_count, preprocess)
audio_processor = input_data.AudioProcessor(None, None, 0, 0, '', 0, 0,
                                            model_settings, None)

results = audio_processor.get_features_for_wav(input_wav, model_settings,
                                               sess)
features = results[0]

variable_base = os.path.splitext(os.path.basename(input_wav).lower())[0]

# Save a C source file containing the feature data as an array.
with gfile.GFile(output_c_file, 'w') as f:
    f.write('/* File automatically created by\n')
    f.write(' * tensorflow/examples/speech_commands/wav_to_features.py \\\n')
    f.write(' * --sample_rate=%d \\\n' % sample_rate)
    f.write(' * --clip_duration_ms=%d \\\n' % clip_duration_ms)
    f.write(' * --window_size_ms=%d \\\n' % window_size_ms)
    f.write(' * --window_stride_ms=%d \\\n' % window_stride_ms)
    f.write(' * --feature_bin_count=%d \\\n' % feature_bin_count)
    if quantize:
        f.write(' * --quantize=1 \\\n')
    f.write(' * --preprocess="%s" \\\n' % preprocess)
    f.write(' * --input_wav="%s" \\\n' % input_wav)
    f.write(' * --output_c_file="%s" \\\n' % output_c_file)
    f.write(' */\n\n')
    f.write('const int g_%s_width = %d;\n' %
            (variable_base, model_settings['fingerprint_width']))
    f.write('const int g_%s_height = %d;\n' %
            (variable_base, model_settings['spectrogram_length']))
    if quantize:
        features_min, features_max = input_data.get_features_range(model_settings)
        f.write('const unsigned char g_%s_data[] = {' % variable_base)
        i = 0
        for value in features.flatten():
            quantized_value = int(
                round(
                    (255 * (value - features_min)) / (features_max - features_min)))
            if quantized_value < 0:
                quantized_value = 0
            if quantized_value > 255:
                quantized_value = 255
            if i == 0:
                f.write('\n  ')
            f.write('%d, ' % (quantized_value))
            i = (i + 1) % 10
    else:
        f.write('const float g_%s_data[] = {\n' % variable_base)
        i = 0
        for value in features.flatten():
            if i == 0:
                f.write('\n  ')
            f.write('%f, ' % value)
            i = (i + 1) % 10
    f.write('\n};\n')
