# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
"""Asserts `inputs` are of the correct type. Should be called in call()."""
if self._assert_type:
    inputs_flattened = nest.flatten(inputs)
    for inp in inputs_flattened:
        assert inp.dtype.base_dtype == self._assert_type, (
            'Input tensor has type %s which does not match assert type %s' %
            (inp.dtype.name, self._assert_type))
