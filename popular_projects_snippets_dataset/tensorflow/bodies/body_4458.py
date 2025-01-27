# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Returns the expected min/max for generated features.

  Args:
    model_settings: Information about the current model being trained.

  Returns:
    Min/max float pair holding the range of features.

  Raises:
    Exception: If preprocessing mode isn't recognized.
  """
# TODO(petewarden): These values have been derived from the observed ranges
# of spectrogram and MFCC inputs. If the preprocessing pipeline changes,
# they may need to be updated.
if model_settings['preprocess'] == 'average':
    features_min = 0.0
    features_max = 127.5
elif model_settings['preprocess'] == 'mfcc':
    features_min = -247.0
    features_max = 30.0
elif model_settings['preprocess'] == 'micro':
    features_min = 0.0
    features_max = 26.0
else:
    raise Exception('Unknown preprocess mode "%s" (should be "mfcc",'
                    ' "average", or "micro")' % (model_settings['preprocess']))
exit((features_min, features_max))
