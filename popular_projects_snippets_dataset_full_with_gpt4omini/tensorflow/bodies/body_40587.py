# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
super(DynamicClusterTest, self).setUp()
os.environ["TF_ENABLE_EAGER_CLIENT_STREAMING_ENQUEUE"] = str(False)
local_port = pywrap_tfe.TF_PickUnusedPortOrDie()
context.set_server_def(
    server_def=get_server_def(
        JOB_NAME,
        local_server_port=local_port,
        remote_server_addresses=[
            self._cached_server1_target, self._cached_server2_target
        ],
        task_index=0))
