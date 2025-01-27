# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Creates a `tf.train.ServerDef` protocol buffer.

  Args:
    server_or_cluster_def: A `tf.train.ServerDef` or `tf.train.ClusterDef`
      protocol buffer, or a `tf.train.ClusterSpec` object, describing the server
      to be defined and/or the cluster of which it is a member.
    job_name: (Optional.) Specifies the name of the job of which the server is a
      member. Defaults to the value in `server_or_cluster_def`, if specified.
    task_index: (Optional.) Specifies the task index of the server in its job.
      Defaults to the value in `server_or_cluster_def`, if specified. Otherwise
      defaults to 0 if the server's job has only one task.
    protocol: (Optional.) Specifies the protocol to be used by the server.
      Acceptable values include `"grpc", "grpc+verbs"`. Defaults to the value in
      `server_or_cluster_def`, if specified. Otherwise defaults to `"grpc"`.
    config: (Options.) A `tf.compat.v1.ConfigProto` that specifies default
      configuration options for all sessions that run on this server.

  Returns:
    A `tf.train.ServerDef`.

  Raises:
    TypeError: If the arguments do not have the appropriate type.
    ValueError: If an argument is not specified and cannot be inferred.
  """
server_def = tensorflow_server_pb2.ServerDef()
if isinstance(server_or_cluster_def, tensorflow_server_pb2.ServerDef):
    server_def.MergeFrom(server_or_cluster_def)
    if job_name is not None:
        server_def.job_name = job_name
    if task_index is not None:
        server_def.task_index = task_index
    if protocol is not None:
        server_def.protocol = protocol
    if config is not None:
        server_def.default_session_config.MergeFrom(config)
else:
    try:
        cluster_spec = ClusterSpec(server_or_cluster_def)
    except TypeError:
        raise TypeError("Could not convert `server_or_cluster_def` to a "
                        "`tf.train.ServerDef` or `tf.train.ClusterSpec`.")
    if job_name is None:
        if len(cluster_spec.jobs) == 1:
            job_name = cluster_spec.jobs[0]
        else:
            raise ValueError("Must specify an explicit `job_name`.")
    if task_index is None:
        task_indices = cluster_spec.task_indices(job_name)
        if len(task_indices) == 1:
            task_index = task_indices[0]
        else:
            raise ValueError("Must specify an explicit `task_index`.")
    if protocol is None:
        protocol = "grpc"

    server_def = tensorflow_server_pb2.ServerDef(
        cluster=cluster_spec.as_cluster_def(),
        job_name=job_name,
        task_index=task_index,
        protocol=protocol)
    if config is not None:
        server_def.default_session_config.MergeFrom(config)
exit(server_def)
