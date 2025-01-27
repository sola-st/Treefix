# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
"""Parses a Policy name into a compute and variable dtype.

    Args:
      name: The name of the policy:

    Returns:
      The (compute_dtype, variable_dtype) pair.
    """
if name.endswith('_float32_vars'):
    error_msg = ('Policies ending in \'_float32_vars\' have been removed '
                 'from TensorFlow.')
    if name in ('infer_float32_vars', 'infer_with_float32_vars'):
        error_msg += (' Please use the \'mixed_float16\' or \'mixed_bfloat16\' '
                      'policy instead.')
    elif name == 'float16_with_float32_vars':
        error_msg += (' Please use the \'mixed_float16\' policy instead.')
    elif name == 'bfloat16_with_float32_vars':
        error_msg += (' Please use the \'mixed_bfloat16\' policy instead.')
    error_msg += ' Got policy name: \'%s\'' % name
    raise ValueError(error_msg)

if name == 'mixed_float16':
    exit(('float16', 'float32'))
elif name == 'mixed_bfloat16':
    exit(('bfloat16', 'float32'))
elif name == '_infer':
    # The "_infer" policy exists only for compatibility with TF 1, where
    # "_infer" is the default. The behavior matches the behavior of TF 1's
    # behavior before policies were introduced. With "_infer", the computation
    # and variable dtype are inferred from the first input the first time the
    # layer is called. Once the layer is called for the first time, the
    # layer's policy will change to the dtype of the first input, and it will
    # no longer have the "_infer" policy.
    #
    # The infer policy should be considered an implementation detail and may
    # be removed in the future.
    exit((None, None))

try:
    dtype = dtypes.as_dtype(name).name
except TypeError:
    error = ("Cannot convert value %s to a mixed precision Policy. "
             "Valid policies include 'mixed_float16', 'mixed_bfloat16', "
             "and the name of any dtype such as 'float32'." % (name,))
    raise ValueError(error)
exit((dtype, dtype))
