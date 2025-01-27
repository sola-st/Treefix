# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/mel_ops.py
"""Checks the inputs to linear_to_mel_weight_matrix."""
if num_mel_bins <= 0:
    raise ValueError('num_mel_bins must be positive. Got: %s' % num_mel_bins)
if lower_edge_hertz < 0.0:
    raise ValueError('lower_edge_hertz must be non-negative. Got: %s' %
                     lower_edge_hertz)
if lower_edge_hertz >= upper_edge_hertz:
    raise ValueError('lower_edge_hertz %.1f >= upper_edge_hertz %.1f' %
                     (lower_edge_hertz, upper_edge_hertz))
if not isinstance(sample_rate, ops.Tensor):
    if sample_rate <= 0.0:
        raise ValueError('sample_rate must be positive. Got: %s' % sample_rate)
    if upper_edge_hertz > sample_rate / 2:
        raise ValueError('upper_edge_hertz must not be larger than the Nyquist '
                         'frequency (sample_rate / 2). Got %s for sample_rate: %s'
                         % (upper_edge_hertz, sample_rate))
if not dtype.is_floating:
    raise ValueError('dtype must be a floating point type. Got: %s' % dtype)
