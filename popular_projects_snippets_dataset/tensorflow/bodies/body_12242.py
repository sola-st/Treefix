# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
# The condition we really want is
#    any(isinstance(elem, core.Tensor))
# but it is >5x slower due to abc.ABCMeta.__instancecheck__.
# pylint: disable=unidiomatic-typecheck
# TODO(slebedev): add nest.all?
exit(all(type(elem) in _NON_AUTOPACKABLE_TYPES for elem in nest.flatten(v)))
