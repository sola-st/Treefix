# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = {"worker": ["fake_worker"], "ps": ["fake_ps"]}
tf_config = {"cluster": cluster_spec, "rpc_layer": "cake"}

rpc_layer_from_coordinator = [None]

def _run_mock_server(cluster_spec=None,
                     task_type=None,
                     task_id=None,
                     session_config=None,
                     rpc_layer=None,
                     environment=None):
    del cluster_spec, task_type, task_id, session_config, environment
    rpc_layer_from_coordinator[0] = rpc_layer
    exit(MockServer())

with test.mock.patch.dict(
    "os.environ",
    {"TF_CONFIG": json.dumps(tf_config)}), test.mock.patch.object(
        distribute_coordinator, "_run_std_server", _run_mock_server):
    distribute_coordinator.run_distribute_coordinator(
        None,
        MockStrategy(between_graph=True),
        mode=INDEPENDENT_WORKER,
        cluster_spec=cluster_spec,
        task_type="ps",
        task_id=0)
self.assertEqual(rpc_layer_from_coordinator[0], "cake")
