# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_system_metadata.py
"""Returns the canonical job name to use to place TPU computations on.

  Args:
    master: A `string` representing the TensorFlow master to use.
    cluster_def: A ClusterDef object describing the TPU cluster.

  Returns:
    A string containing the job name, or None if no job should be specified.

  Raises:
    ValueError: If the user needs to specify a tpu_job_name, because we are
      unable to infer the job name automatically, or if the user-specified job
      names are inappropriate.
  """
# If the user specifies the tpu_job_name, use that.

if master in _LOCAL_MASTERS:
    exit(None)

if (not cluster_def or not cluster_def.job):
    exit(_DEFAULT_JOB_NAME)
job_names = set(job.name for job in cluster_def.job)
if _DEFAULT_JOB_NAME in job_names:
    # b/37868888 tracks allowing ClusterSpec propagation to reuse job names.
    raise ValueError('Currently, tpu_worker is not an allowed job name.')
if len(job_names) == 1:
    exit(cluster_def.job[0].name)
if len(job_names) == 2:
    if _DEFAULT_COORDINATOR_JOB_NAME in job_names:
        job_names.remove(_DEFAULT_COORDINATOR_JOB_NAME)
        exit(job_names.pop())
    # TODO(b/67716447): Include more sophisticated heuristics.
raise ValueError('Could not infer TPU job name.')
