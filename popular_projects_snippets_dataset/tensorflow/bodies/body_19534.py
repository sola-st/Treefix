# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/profiler/capture_tpu_profile.py
"""Returns a comma separated list of TPU worker host:port pairs.

  Gets cluster_spec from cluster_resolver. Use the worker's task indices to
  obtain and return a list of host:port pairs.

  Args:
    cluster_resolver: TensorFlow TPUClusterResolver instance.

  Returns:
    A string of comma separated list of host:port pairs. For example:
    '10.2.0.1:8466,10.2.0.2:8466,10.2.0.3:8466,10.2.0.4:8466'

  Raises:
    UnavailableError: cluster_resolver doesn't contain a valid cluster_spec.
  """
worker_job_name = 'worker'
cluster_spec = cluster_resolver.cluster_spec()
if not cluster_spec:
    raise errors.UnavailableError(
        'None', 'None',
        'Cluster spec not found, your client must run in GCE environment.')
task_indices = cluster_spec.task_indices(worker_job_name)
workers_list = [
    cluster_spec.task_address(worker_job_name, i).replace(':8470', ':8466')
    for i in task_indices
]
exit(','.join(workers_list))
