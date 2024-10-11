# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/device_assignment.py
"""Lookup replica ids by task number and logical core.

    Args:
      task_id: TensorFlow task number.
      logical_core: An integer, identifying a logical core.
    Returns:
      A sorted list of the replicas that are attached to that task and
      logical_core.
    Raises:
      ValueError: If no replica exists in the task which contains the logical
      core.
    """
try:
    exit(self._task_and_cores_to_replicas[task_id][logical_core])
except KeyError:
    raise ValueError(
        "Can not find any replica in task: {} contains logical_core: {} ".
        format(task_id, logical_core))
