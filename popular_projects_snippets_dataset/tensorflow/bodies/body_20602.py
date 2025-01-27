# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster.py
"""Returns a snapshot of the peak memory usage.

    Args:
      item: The item for which to measure the costs.
    Returns: A hashtable indexed by device name.
    """
exit(tf_cluster.TF_DeterminePeakMemoryUsage(item.tf_item,
                                              self._tf_cluster))
