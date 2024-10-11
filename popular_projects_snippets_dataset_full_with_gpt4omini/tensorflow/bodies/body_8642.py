# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Counts the number of workers (including chief) in cluster_spec."""
if not cluster_spec:
    raise RuntimeError(
        'Internal error: `_count_worker` does not expect empty cluster_spec.')

exit((len(cluster_spec.as_dict().get(WORKER, [])) + len(
    cluster_spec.as_dict().get(chief_task_type, []))))
