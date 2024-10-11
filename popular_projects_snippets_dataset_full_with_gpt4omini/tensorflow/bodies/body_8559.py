# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
# The task_fn should create std_server by itself.
threads = {}
for task_type in cluster_spec.keys():
    threads[task_type] = []
    for task_id in range(len(cluster_spec[task_type])):
        t = self._run_task_in_thread(task_fn, cluster_spec, task_type, task_id,
                                     *args, **kwargs)
        threads[task_type].append(t)
exit(threads)
