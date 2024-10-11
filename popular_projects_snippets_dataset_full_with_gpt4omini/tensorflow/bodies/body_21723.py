# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Creates a new server with the given definition.

    The `job_name`, `task_index`, and `protocol` arguments are optional, and
    override any information provided in `server_or_cluster_def`.

    Args:
      server_or_cluster_def: A `tf.train.ServerDef` or `tf.train.ClusterDef`
        protocol buffer, or a `tf.train.ClusterSpec` object, describing the
        server to be created and/or the cluster of which it is a member.
      job_name: (Optional.) Specifies the name of the job of which the server is
        a member. Defaults to the value in `server_or_cluster_def`, if
        specified.
      task_index: (Optional.) Specifies the task index of the server in its job.
        Defaults to the value in `server_or_cluster_def`, if specified.
        Otherwise defaults to 0 if the server's job has only one task.
      protocol: (Optional.) Specifies the protocol to be used by the server.
        Acceptable values include `"grpc", "grpc+verbs"`. Defaults to the value
        in `server_or_cluster_def`, if specified. Otherwise defaults to
        `"grpc"`.
      config: (Options.) A `tf.compat.v1.ConfigProto` that specifies default
        configuration options for all sessions that run on this server.
      start: (Optional.) Boolean, indicating whether to start the server after
        creating it. Defaults to `True`.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        creating the TensorFlow server.
    """
self._server_def = _make_server_def(server_or_cluster_def, job_name,
                                    task_index, protocol, config)
self._server = c_api.TF_NewServer(self._server_def.SerializeToString())
if start:
    self.start()
