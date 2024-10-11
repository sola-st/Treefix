# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Run `cmd_args` in a process for each task in `cluster_spec`."""
processes = {}
for task_type in cluster_spec.keys():
    processes[task_type] = []
    for task_id in range(len(cluster_spec[task_type])):
        p = self._run_task_in_process(cmd_args, cluster_spec, task_type,
                                      task_id)
        processes[task_type].append(p)
exit(processes)
