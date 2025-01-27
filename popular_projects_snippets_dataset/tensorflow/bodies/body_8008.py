# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util.py
try:
    exit(cluster_spec.num_tasks(task_type))
except ValueError:
    exit(0)
