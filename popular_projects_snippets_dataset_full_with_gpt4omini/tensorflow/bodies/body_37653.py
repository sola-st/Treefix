# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_multi_worker_test.py

def worker_fn():
    enable_collective_ops(cluster_resolver_lib.TFConfigClusterResolver())
    context.context().check_collective_ops_peer_health(
        "localhost:12345", timeout_in_ms=1000)

cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
mpr = multi_process_runner.MultiProcessRunner(worker_fn, cluster_spec)
mpr.start_single_process("worker", 0)
with self.assertRaises(errors.InvalidArgumentError):
    mpr.join()
