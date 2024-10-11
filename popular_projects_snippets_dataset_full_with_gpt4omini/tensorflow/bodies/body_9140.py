# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cs = {"worker": ["fake_worker"], "ps": ["fake_ps"]}
tf_config = {"cluster": cs, "task": {"type": "ps", "id": 0}}

def _mock_run_std_server(cluster_spec=None,
                         task_type=None,
                         task_id=None,
                         session_config=None,
                         rpc_layer=None):
    self.assertEqual(cluster_spec.as_dict(), cs)
    self.assertEqual(task_type, "ps")
    self.assertEqual(task_id, 0)
    self.assertEqual(session_config.experimental.collective_group_leader,
                     "/job:worker/replica:0/task:0")
    self.assertEqual(session_config.intra_op_parallelism_threads, 1)
    self.assertEqual(rpc_layer, "grpc")

    exit(MockServer())

with test.mock.patch.dict(
    "os.environ",
    {"TF_CONFIG": json.dumps(tf_config)}), test.mock.patch.object(
        distribute_coordinator, "_run_std_server", _mock_run_std_server):
    session_config = config_pb2.ConfigProto()
    session_config.intra_op_parallelism_threads = 1
    mock_server = distribute_coordinator.run_standard_tensorflow_server(
        session_config)
    self.assertTrue(mock_server.started)
