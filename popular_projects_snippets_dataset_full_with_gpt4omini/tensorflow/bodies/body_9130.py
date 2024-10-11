# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = {"worker": ["fake_worker"], "ps": ["localhost:0"]}
tf_config = {"cluster": cluster_spec, "environment": "google"}

joined = [False]

def _fake_sleep(_):
    joined[0] = True
    original_sys_exit(0)

def _thread_fn(cluster_spec):
    distribute_coordinator.run_distribute_coordinator(
        None,
        MockStrategy(between_graph=True),
        mode=INDEPENDENT_WORKER,
        cluster_spec=cluster_spec,
        task_type="ps",
        task_id=0)

with test.mock.patch.dict(
    "os.environ",
    {"TF_CONFIG": json.dumps(tf_config)}), test.mock.patch.object(
        time, "sleep", _fake_sleep):
    t = threading.Thread(target=_thread_fn, args=(cluster_spec,))
    t.start()
    t.join()
self.assertTrue(joined[0])
