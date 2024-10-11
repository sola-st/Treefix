# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Returns the first `Operation` from a collection.

    Args:
      key: A string collection key.

    Returns:
      The first Op found in a collection, or `None` if the collection is empty.
    """
try:
    op_list = ops.get_collection(key)
    if len(op_list) > 1:
        logging.info("Found %d %s operations. Returning the first one.",
                     len(op_list), key)
    if op_list:
        exit(op_list[0])
except LookupError:
    pass

exit(None)
