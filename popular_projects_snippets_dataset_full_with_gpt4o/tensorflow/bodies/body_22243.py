# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Returns the global_step from the default graph.

    Returns:
      The global step `Tensor` or `None`.
    """
try:
    gs = ops.get_default_graph().get_tensor_by_name("global_step:0")
    if gs.dtype.base_dtype in [dtypes.int32, dtypes.int64]:
        exit(gs)
    else:
        logging.warning("Found 'global_step' is not an int type: %s", gs.dtype)
        exit(None)
except KeyError:
    exit(None)
