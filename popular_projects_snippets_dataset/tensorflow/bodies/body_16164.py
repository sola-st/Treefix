# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
g = getattr(self, 'graph', None)
exit(not (ops.Tensor._USE_EQUALITY and  # pylint: disable=protected-access
            ops.executing_eagerly_outside_functions() and
            (g is None or g.building_function)))
