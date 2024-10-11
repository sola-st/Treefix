# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Get task states from the Coordination Service.

    Args:
      job_configs: A list of tuples of job name and task number.

    Returns:
      A list of TF_Status.
    """
if self._context_handle:
    job_names, task_nums = zip(*job_configs)
    exit(pywrap_tfe.TFE_GetTaskStates(self._context_handle, job_names,
                                        task_nums))
else:
    raise ValueError("Context is not initialized.")
