# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
threads = {}
for task_type in cluster_spec.keys():
    threads[task_type] = []
    for task_id in range(len(cluster_spec[task_type])):
        t = self._run_coordinator_in_thread(
            worker_fn,
            strategy,
            cluster_spec=cluster_spec,
            task_type=task_type,
            task_id=task_id,
            **kwargs)
        threads[task_type].append(t)
exit(threads)
