# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
devices = config.list_logical_devices("GPU")
per_worker_gpus = {}
for d in devices:
    d_spec = tf_device.DeviceSpec.from_string(d.name)
    if d_spec.device_type == "GPU" and d_spec.job == "worker":
        # TODO(b/167894802): update if worker name is customizable
        job_spec = d_spec.replace(device_type=None, device_index=None)
        per_worker_gpus[job_spec] = per_worker_gpus.get(job_spec, 0) + 1

num_gpus = 0
for _, count in per_worker_gpus.items():
    if num_gpus > 0 and count != num_gpus:
        raise ValueError("Mismatched number of GPUs per worker")
    num_gpus = count

self._num_gpus_per_worker = num_gpus
logging.info(f"Number of GPUs on workers: {self._num_gpus_per_worker}")
