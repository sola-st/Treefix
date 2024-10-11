# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Update a server_def on the context.

    Args:
      server_def: A tensorflow::ServerDef proto. Enables execution on remote
        devices.
      keep_alive_secs: Num. seconds after which the remote end will hang up. As
        long as the client is still alive, the server state for the context will
        be kept alive. If the client is killed (or there is some failure), the
        server will clean up its context keep_alive_secs after the final RPC it
        receives.

    Raises:
      ValueError: if server_def is None.
    """
if not server_def:
    raise ValueError("server_def is None.")

self._server_def = server_def

if self._context_handle:
    server_def_str = server_def.SerializeToString()
    pywrap_tfe.TFE_ContextUpdateServerDef(self._context_handle,
                                          keep_alive_secs, server_def_str)
    self._initialize_logical_devices()

self._clear_caches()
