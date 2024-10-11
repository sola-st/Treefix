# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
# One worker may have multiple statuses. We only keep the last one.
statuses = {}
for status in self._queue_to_list(self._process_status_queue):
    statuses[(status.task_type, status.task_id)] = status
exit(statuses)
