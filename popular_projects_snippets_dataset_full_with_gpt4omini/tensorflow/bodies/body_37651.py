# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_multi_worker_test.py

def worker_fn():
    cluster_resolver = cluster_resolver_lib.TFConfigClusterResolver()
    enable_collective_ops(cluster_resolver)

    collective_ops.all_reduce(
        constant_op.constant(1.),
        group_size=2,
        group_key=100,
        instance_key=100,
        merge_op="Add",
        final_op="Id",
        communication_hint="ring")

    if cluster_resolver.task_type == "worker":
        # MultiProcessRunner will auto restart worker-0.
        os._exit(1)  # pylint: disable=protected-access
    else:
        # chief should eventually gets FailedPreconditionError after worker-0
        # has restarted.
        while True:
            time.sleep(1)
            try:
                context.context().check_collective_ops_peer_health(
                    "/job:worker/replica:0/task:0", timeout_in_ms=1000)
            except errors.UnavailableError:
                pass
            except errors.FailedPreconditionError:
                break

cluster_spec = multi_worker_test_base.create_cluster_spec(
    has_chief=True, num_workers=1)
mpr = multi_process_runner.MultiProcessRunner(
    worker_fn, cluster_spec, auto_restart=True)
mpr.start()
mpr.join()
