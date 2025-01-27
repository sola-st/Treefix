# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
"""Return a `tf.compat.v1.ConfigProto` that ensures we use the RPC stack for tests.

    This configuration ensures that we continue to exercise the gRPC
    stack when testing, rather than using the in-process optimization,
    which avoids using gRPC as the transport between a client and
    master in the same process.

    Returns:
      A `tf.compat.v1.ConfigProto`.
    """
exit(config_pb2.ConfigProto(rpc_options=rpc_options_pb2.RPCOptions(
    use_rpc_for_inprocess_master=True)))
