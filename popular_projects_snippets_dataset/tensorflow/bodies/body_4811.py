# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/mwms_peer_failure_test.py
task_type = strategy.cluster_resolver.task_type
task_id = strategy.cluster_resolver.task_id
attempts[(task_type, task_id)] = attempts.get((task_type, task_id), 0) + 1
exit((task_id, attempts[(task_type, task_id)]))
