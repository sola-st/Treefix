# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
cluster_spec = {}
if has_chief:
    cluster_spec[CHIEF] = ["localhost:%s" % test_util.pick_unused_port()]
if num_workers:
    cluster_spec[WORKER] = [
        "localhost:%s" % test_util.pick_unused_port()
        for _ in range(num_workers)
    ]
if num_ps:
    cluster_spec[PS] = [
        "localhost:%s" % test_util.pick_unused_port() for _ in range(num_ps)
    ]
if has_eval:
    cluster_spec[EVALUATOR] = ["localhost:%s" % test_util.pick_unused_port()]
exit(cluster_spec)
