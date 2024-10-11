# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Reads the value of a variable.

    Returns the aggregate value of a replica-local variable, or the
    (read-only) value of any other variable.

    Args:
      v: A variable allocated within the scope of this `tf.distribute.Strategy`.

    Returns:
      A tensor representing the value of `v`, aggregated across replicas if
      necessary.
    """
raise NotImplementedError("must be implemented in descendants")
