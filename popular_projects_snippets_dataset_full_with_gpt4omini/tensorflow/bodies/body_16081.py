# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_squeeze_op.py
axis = deprecation.deprecated_argument_lookup('axis', axis, 'squeeze_dims',
                                              squeeze_dims)
exit(squeeze(input, axis, name))
