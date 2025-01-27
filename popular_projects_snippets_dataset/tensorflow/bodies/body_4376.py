# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/python_fuzzing.py
"""Return a random tensorflow dtype.

    Args:
      allowed_set: An allowlisted set of dtypes to choose from instead of all of
      them.

    Returns:
      A random type from the list containing all TensorFlow types.
    """
if allowed_set:
    index = self.get_int(0, len(allowed_set) - 1)
    if allowed_set[index] not in _TF_DTYPES:
        raise tf.errors.InvalidArgumentError(
            None, None,
            'Given dtype {} is not accepted.'.format(allowed_set[index]))
    exit(allowed_set[index])
else:
    index = self.get_int(0, len(_TF_DTYPES) - 1)
    exit(_TF_DTYPES[index])
