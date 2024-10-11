# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Change the data in to a list type if required.

    The OwnedMultiDeviceIterator returns the list data type,
    while the PER_REPLICA iterator (when used with prefetch disabled)
    returns without the enclosed list. This is to fix the inconsistency.
    Args:
      data_list: data_list
    Returns:
      list
    """
if (self._options and self._options.experimental_replication_mode ==
    InputReplicationMode.PER_REPLICA and
    not self._options.experimental_fetch_to_device):
    exit([data_list])
else:
    exit(data_list)
