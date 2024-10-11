# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/accelerator_util.py
"""Initialize GRPC servers and collectives for multi-client DTensor setup.

  This function can be used to initialize a multi-client cluster and enable
  collective ops. GRPC servers are necessary in the multi-client mode, even
  when the number of clientis is 1.

  NOTE: this function must be called in an eager context.

  Args:
    job_name: The job name used by all clients in the DTensor cluster.
    dtensor_jobs: A list of the DTensor client jobs participating in the
      cluster. Must be strings of the form "hostname:port".
    client_id: The ID of the DTensor client this function is being called in.
    collective_leader: The job/task that will be used to run collectives.
    port: The port this client's GRPC server will run on. If omitted, use the
      port from dtensor_jobs for this client.
    gpu_use_nccl_communication: if True, configure TensorFlow to use NCCL by
      default.
    enable_coordination_service: If true, enable distributed coordination
      service to make sure that workers know the devices on each other, a
      prerequisite for data transfer through cross-worker rendezvous.

  Raises:
    RuntimeError: If running inside a tf.function.
  """
assert context.executing_eagerly()

if not collective_leader.startswith("/job:"):
    collective_leader = "/job:" + collective_leader

context.context().configure_collective_ops(
    use_nccl_communication=gpu_use_nccl_communication,
    collective_leader=collective_leader)
if enable_coordination_service:
    context.context().configure_coordination_service(
        service_type="standalone", service_leader=collective_leader)

config_proto = context.get_config()

# Construct server def from the host directly instead of relying on
# TF_CONFIG.
cluster_def = cluster_pb2.ClusterDef()
# Note that for bns addresses, we will currently rely on the sorted string
# of job name as the order of assigning task ids. This might be brittle once
# we have jobs across multiple cells.
cluster_def.job.add(name=job_name, tasks=dict(enumerate(dtensor_jobs)))
server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_def,
    default_session_config=config_proto,
    job_name=job_name,
    task_index=client_id,
    protocol=remote_utils.get_default_communication_protocol(),
    port=port)
server_def.default_session_config.rpc_options.num_channels_per_target = 4
server_def.default_session_config.experimental.recv_buf_max_chunk = -1

logging.info("Enabling collectives with server_def: %s", server_def)

context.context().enable_collective_ops(server_def)

context.ensure_initialized()
