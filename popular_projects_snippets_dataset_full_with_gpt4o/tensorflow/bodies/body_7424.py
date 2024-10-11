# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Method for registering tf.function on server.

    Registered methods can be invoked remotely from clients.

    Args:
      method_name: Name of the tf.function. Clients use this method_name to make
        RPCs.
      func: A `tf.function` or ConcreteFunction to register.
    """
raise NotImplementedError("Please use create_server method to create a"
                          "concrete subclass of Server.")
