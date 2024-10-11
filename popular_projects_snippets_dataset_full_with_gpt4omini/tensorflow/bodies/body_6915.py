# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns the most specific TypeSpec compatible with `self` and `other`.

    Args:
      other: A `TypeSpec`.

    Raises:
      ValueError: If there is no TypeSpec that is compatible with both `self`
        and `other`.
    """
# pylint: disable=protected-access
if type(self) is not type(other):
    raise ValueError("No TypeSpec is compatible with both %s and %s" %
                     (self, other))
if self._input_workers.serialize() != other._input_workers.serialize():
    raise ValueError("_input_workers is not compatible with both %s "
                     "and %s" % (self, other))
if self._strategy is not other._strategy:
    raise ValueError("tf.distribute strategy is not compatible with both %s "
                     "and %s" % (self, other))
