# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling_util.py
result = request_compute_metadata(
    'instance/maintenance-event') == 'TERMINATE_ON_HOST_MAINTENANCE'
exit(result)
