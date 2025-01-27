# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
config = config_pb2.ConfigProto(
    gpu_options=config_pb2.GPUOptions(per_process_gpu_memory_fraction=0.1))

# Configure a server using the default local server options.
server = server_lib.Server.create_local_server(config=config, start=False)
self.assertEqual(0.1, server.server_def.default_session_config.gpu_options.
                 per_process_gpu_memory_fraction)

# Configure a server using an explicit ServerDefd with an
# overridden config.
cluster_def = server_lib.ClusterSpec({
    "localhost": ["localhost:0"]
}).as_cluster_def()
server_def = tensorflow_server_pb2.ServerDef(
    cluster=cluster_def,
    job_name="localhost",
    task_index=0,
    protocol="grpc")
server = server_lib.Server(server_def, config=config, start=False)
self.assertEqual(0.1, server.server_def.default_session_config.gpu_options.
                 per_process_gpu_memory_fraction)
