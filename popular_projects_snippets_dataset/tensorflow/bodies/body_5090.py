# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
del task_type, task_id

if session_config:
    session_config.CopyFrom(self._update_config_proto(session_config))

if cluster_spec:
    # TODO(yuefengz): remove the following code once cluster_resolver is
    # added.
    num_gpus_per_worker = _infer_num_gpus_per_worker(self._devices)
    multi_worker_devices = _cluster_spec_to_device_list(
        cluster_spec, num_gpus_per_worker)
    self._initialize_multi_worker(multi_worker_devices)
