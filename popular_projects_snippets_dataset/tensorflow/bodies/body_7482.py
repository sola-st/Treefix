# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
for process_status in process_statuses.values():
    assert isinstance(process_status, _ProcessStatusInfo)
    if not process_status.is_successful:
        process_status.exc_info[1].mpr_result = self._get_mpr_result(
            process_statuses)
        six.reraise(*process_status.exc_info)
