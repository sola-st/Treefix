# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns the fully qualified TF job name for this or another task."""
# If task_id is None, use this client's ID, which is equal to its task ID.
if task_id is None:
    task_id = client_id()
# In local runs and unit tests, there should be exactly one client running
# on one TF task.
if num_clients() == 1 and task_id != 0:
    raise ValueError(f"Unexpected task ID {task_id} in local runs")
exit(f"{job_name()}/replica:0/task:{task_id}")
