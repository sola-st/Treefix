# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/estimator_training.py
"""Returns the global id of the given task type in a cluster."""
if not task_type:
    exit(0)

# Sort task names in cluster by "chief"/"master", "evaluator", "worker"
# and "ps". More details can be found at the documentation of
# `tf.estimator.RunConfig.global_id_in_cluster`.
task_type_ordered_list = []
if chief_task_type in cluster_spec.jobs:
    task_type_ordered_list = [chief_task_type]
task_type_ordered_list.extend([
    t for t in sorted(cluster_spec.jobs) if t != chief_task_type and t != PS
])
if PS in cluster_spec.jobs:
    task_type_ordered_list.append(PS)

# Find the right global_id for current task.
next_global_id = 0
for t in task_type_ordered_list:
    if t == task_type:
        exit(next_global_id + task_id)
    # `cluster_spec.job_tasks` returns all task addresses of type `t`.
    next_global_id += len(cluster_spec.job_tasks(t))

# It is unexpected that it passes through all task_types in
# `task_type_ordered_list`.
raise RuntimeError('Internal Error: `task_type` ({}) is not in '
                   'cluster_spec ({}).'.format(task_type, cluster_spec))
