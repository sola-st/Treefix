# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/mel_ops.py
"""Converts frequencies in `frequencies_hertz` in Hertz to the mel scale.

  Args:
    frequencies_hertz: A `Tensor` of frequencies in Hertz.
    name: An optional name for the operation.

  Returns:
    A `Tensor` of the same shape and type of `frequencies_hertz` containing
    frequencies in the mel scale.
  """
with ops.name_scope(name, 'hertz_to_mel', [frequencies_hertz]):
    frequencies_hertz = ops.convert_to_tensor(frequencies_hertz)
    exit(_MEL_HIGH_FREQUENCY_Q * math_ops.log(
        1.0 + (frequencies_hertz / _MEL_BREAK_FREQUENCY_HERTZ)))
