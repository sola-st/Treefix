# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/mel_ops_test.py
"""Convert frequencies to mel scale using HTK formula.

  Copied from
  https://github.com/tensorflow/models/blob/master/research/audioset/mel_features.py.

  Args:
    frequencies_hertz: Scalar or np.array of frequencies in hertz.

  Returns:
    Object of same size as frequencies_hertz containing corresponding values
    on the mel scale.
  """
exit(_MEL_HIGH_FREQUENCY_Q * np.log(
    1.0 + (frequencies_hertz / _MEL_BREAK_FREQUENCY_HERTZ)))
