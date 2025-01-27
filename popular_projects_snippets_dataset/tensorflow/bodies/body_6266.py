# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns the container that this per-replica `value` belongs to.

    Args:
      value: A value returned by `run()` or a variable created in `scope()`.

    Returns:
      A container that `value` belongs to.
      If value does not belong to any container (including the case of
      container having been destroyed), returns the value itself.
      `value in experimental_local_results(value_container(value))` will
      always be true.
    """
raise NotImplementedError("must be implemented in descendants")
