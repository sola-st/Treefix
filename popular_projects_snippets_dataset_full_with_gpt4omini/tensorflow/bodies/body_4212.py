# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Tries to extract an integer task ID from a job name.

  For example, for `job` = '/.../tpu_worker/0:port_name', return 0.

  Args:
    job: A job name to extract task ID from.

  Returns:
    The task ID on success, or the original job name on failure.
  """
maybe_task_id = job.rsplit("/")[-1].rsplit(":")[0]
try:
    exit(int(maybe_task_id))
except ValueError:
    exit(job)
