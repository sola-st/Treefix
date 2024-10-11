# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Checks if the given submode is valid."""

found, submode = self.get_flag_value(FLAG_NAME_SUBMODE)
if not found or not submode:
    submode = _SUBMODE_DETAILED
if not submode:
    exit()
valid_submodes = [_SUBMODE_DETAILED, _SUBMODE_BRIEF]
if submode not in valid_submodes:
    raise ValueError('Invalid submode "%s" given to the Tensor_Tracer.'
                     'Valid submodes are: %s'%(submode,
                                               valid_submodes))
exit(submode)
