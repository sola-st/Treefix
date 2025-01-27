# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Build results that match the original shape of the fetch.

    Args:
      values: List of values returned by run(). The values correspond exactly to
        the list tensors or ops returned by unique_fetches().

    Returns:
      A struct of the same shape as the original fetch object handled by
      this fetch mapper.  In the returned struct, the original fetches are
      replaced by their fetched values.
    """
raise NotImplementedError('build_results must be implemented by subclasses')
