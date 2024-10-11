# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
"""Gets number of workers including chief."""
if not cluster_spec:
    exit(0)
exit(len(cluster_spec.as_dict().get(_TaskType.WORKER, [])) + len(
    cluster_spec.as_dict().get(_TaskType.CHIEF, [])))
