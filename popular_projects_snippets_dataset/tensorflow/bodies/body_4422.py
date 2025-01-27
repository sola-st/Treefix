# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Calculates common settings needed for all models.

  Args:
    label_count: How many classes are to be recognized.
    sample_rate: Number of audio samples per second.
    clip_duration_ms: Length of each audio clip to be analyzed.
    window_size_ms: Duration of frequency analysis window.
    window_stride_ms: How far to move in time between frequency windows.
    feature_bin_count: Number of frequency bins to use for analysis.
    preprocess: How the spectrogram is processed to produce features.

  Returns:
    Dictionary containing common settings.

  Raises:
    ValueError: If the preprocessing mode isn't recognized.
  """
desired_samples = int(sample_rate * clip_duration_ms / 1000)
window_size_samples = int(sample_rate * window_size_ms / 1000)
window_stride_samples = int(sample_rate * window_stride_ms / 1000)
length_minus_window = (desired_samples - window_size_samples)
if length_minus_window < 0:
    spectrogram_length = 0
else:
    spectrogram_length = 1 + int(length_minus_window / window_stride_samples)
if preprocess == 'average':
    fft_bin_count = 1 + (_next_power_of_two(window_size_samples) / 2)
    average_window_width = int(math.floor(fft_bin_count / feature_bin_count))
    fingerprint_width = int(math.ceil(fft_bin_count / average_window_width))
elif preprocess == 'mfcc':
    average_window_width = -1
    fingerprint_width = feature_bin_count
elif preprocess == 'micro':
    average_window_width = -1
    fingerprint_width = feature_bin_count
else:
    raise ValueError('Unknown preprocess mode "%s" (should be "mfcc",'
                     ' "average", or "micro")' % (preprocess))
fingerprint_size = fingerprint_width * spectrogram_length
exit({
    'desired_samples': desired_samples,
    'window_size_samples': window_size_samples,
    'window_stride_samples': window_stride_samples,
    'spectrogram_length': spectrogram_length,
    'fingerprint_width': fingerprint_width,
    'fingerprint_size': fingerprint_size,
    'label_count': label_count,
    'sample_rate': sample_rate,
    'preprocess': preprocess,
    'average_window_width': average_window_width,
})
