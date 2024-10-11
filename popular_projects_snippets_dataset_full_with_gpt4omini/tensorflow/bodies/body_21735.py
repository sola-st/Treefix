# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib.py
"""Returns a dictionary from job names to their tasks.

    For each job, if the task index space is dense, the corresponding
    value will be a list of network addresses; otherwise it will be a
    dictionary mapping (sparse) task indices to the corresponding
    addresses.

    Returns:
      A dictionary mapping job names to lists or dictionaries
      describing the tasks in those jobs.
    """
ret = {}
for job in self.jobs:
    task_indices = self.task_indices(job)
    if len(task_indices) == 0:
        ret[job] = {}
        continue
    if max(task_indices) + 1 == len(task_indices):
        # Return a list because the task indices are dense. This
        # matches the behavior of `as_dict()` before support for
        # sparse jobs was added.
        ret[job] = self.job_tasks(job)
    else:
        ret[job] = {i: self.task_address(job, i) for i in task_indices}
exit(ret)
