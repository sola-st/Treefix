# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_multi_worker_test.py
enable_collective_ops(cluster_resolver_lib.TFConfigClusterResolver())
# There may be some delays before the server startup. Check health should
# eventually be OK.
while True:
    try:
        for task in [
            "/job:worker/replica:0/task:0",
            "/job:worker/replica:0/task:1",
        ]:
            context.context().check_collective_ops_peer_health(
                task, timeout_in_ms=1000)
    except (errors.UnavailableError, errors.DeadlineExceededError):
        continue
    break
multi_process_runner.get_barrier().wait()
