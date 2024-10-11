# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/learning_rate_schedule.py
"""Piecewise constant from boundaries and interval values.

    Args:
      boundaries: A list of `Tensor`s or `int`s or `float`s with strictly
        increasing entries, and with all elements having the same type as the
        optimizer step.
      values: A list of `Tensor`s or `float`s or `int`s that specifies the
        values for the intervals defined by `boundaries`. It should have one
        more element than `boundaries`, and all elements should have the same
        type.
      name: A string. Optional name of the operation. Defaults to
        'PiecewiseConstant'.

    Raises:
      ValueError: if the number of elements in the lists do not match.
    """
super(PiecewiseConstantDecay, self).__init__()

if len(boundaries) != len(values) - 1:
    raise ValueError(
        "The length of boundaries should be 1 less than the length of values")

self.boundaries = boundaries
self.values = values
self.name = name
