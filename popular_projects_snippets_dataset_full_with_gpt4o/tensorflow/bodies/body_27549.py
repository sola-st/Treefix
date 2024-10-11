# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
super(EagerClusterReplicateTest, self).setUp()

# TODO(b/171412104): Move create server to __init__ once tfrt support it.
self._cached_server1 = server_lib.Server.create_local_server()
self._cached_server2 = server_lib.Server.create_local_server()
self._cached_server1_target = self._cached_server1.target[len("grpc://"):]
self._cached_server2_target = self._cached_server2.target[len("grpc://"):]

# Start the local server.
local_port = pywrap_tfe.TF_PickUnusedPortOrDie()
context.set_server_def(
    server_def=_get_server_def(
        self._job_name,
        local_server_port=local_port,
        remote_server_addresses=[
            self._cached_server1_target, self._cached_server2_target
        ],
        task_index=0))
