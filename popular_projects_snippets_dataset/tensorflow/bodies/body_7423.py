# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Create TF RPC server at given address.

    Args:
      rpc_layer: Communication layer between client and server. Only "grpc" rpc
        layer is supported at the moment.
      address: Address where RPC server is hosted.

    Returns:
      An instance of `tf.distribute.experimental.rpc.Server` class.

    Raises:
        A ValueError if rpc_layer other than "grpc" is used. Only GRPC
        is supported at the moment.

    Example usage:

      >>> import portpicker
      >>> @tf.function(input_signature=[
      ...      tf.TensorSpec([], tf.int32),
      ...      tf.TensorSpec([], tf.int32)])
      ... def remote_fn(a, b):
      ...   return tf.add(a, b)

      >>> port = portpicker.pick_unused_port()
      >>> address = "localhost:{}".format(port)
      >>> server = tf.distribute.experimental.rpc.Server.create("grpc", address)
      >>> server.register("addition", remote_fn)
      >>> server.start()

    """
if rpc_layer != "grpc":
    raise ValueError("Only GRPC backend is supported at the moment.")
exit(GrpcServer(address=address))
