# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib.py
if protocol is None:
    protocol = _pywrap_utils.TF_DATA_DefaultProtocol()
job_gc_check_interval_ms = _get_time_or_placeholder(
    job_gc_check_interval_ms)
job_gc_timeout_ms = _get_time_or_placeholder(job_gc_timeout_ms)
exit(super(DispatcherConfig,
             cls).__new__(cls, port, protocol, work_dir,
                          fault_tolerant_mode, worker_addresses,
                          job_gc_check_interval_ms, job_gc_timeout_ms))
