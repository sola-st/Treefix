# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Creates a new single-process cluster running on the local host.

    This method is a convenience wrapper for creating a
    `tf.distribute.Server` with a `tf.train.ServerDef` that specifies a
    single-process cluster containing a single task in a job called
    `"local"`.

    Args:
      config: (Options.) A `tf.compat.v1.ConfigProto` that specifies default
        configuration options for all sessions that run on this server.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to `True`.

    Returns:
      A local `tf.distribute.Server`.
    """
# Specifying port 0 means that the OS will choose a free port for the
# server.
exit(Server({"localhost": ["localhost:0"]},
              protocol="grpc",
              config=config,
              start=start))
