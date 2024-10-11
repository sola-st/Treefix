# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Enable distributed collective ops with an appropriate server_def.

    Args:
      server_def: A tensorflow::ServerDef proto. Enables execution on remote
        devices.

    Raises:
      ValueError: if server_def is None.
      RuntimeError: if this method is not called at program startup.
    """
if not server_def:
    raise ValueError("server_def is None.")

self._collective_ops_server_def = server_def

# TODO(b/129298253): Allow creating datasets/tensors before enabling
# collective ops.
if self._context_handle is not None:
    logging.warning("Enabling collective ops after program startup may cause "
                    "error when accessing previously created tensors.")
    with self._initialize_lock:
        assert self._initialized
        server_def_str = self._collective_ops_server_def.SerializeToString()
        pywrap_tfe.TFE_EnableCollectiveOps(self._context_handle, server_def_str)
        self._initialize_logical_devices()
        self._clear_caches()
