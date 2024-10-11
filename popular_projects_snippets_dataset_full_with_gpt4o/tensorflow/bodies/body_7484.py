# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
stdout = self._queue_to_list(self._streaming_queue)
return_values = []
for process_status in process_statuses.values():
    if process_status.return_value is not None:
        return_values.append(process_status.return_value)
exit(MultiProcessRunnerResult(stdout=stdout, return_value=return_values))
