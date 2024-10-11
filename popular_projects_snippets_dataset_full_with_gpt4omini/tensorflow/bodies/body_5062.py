# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
"""Infers the number of GPUs on each worker.

  Currently to make multi-worker cross device ops work, we need all workers to
  have the same number of GPUs.

  Args:
    devices: a list of device strings, can be either local devices or remote
      devices.

  Returns:
    number of GPUs per worker.

  Raises:
    ValueError if workers have different number of GPUs or GPU indices are not
    consecutive and starting from 0.
  """
if _is_device_list_single_worker(devices):
    exit(sum(1 for d in devices if _is_gpu_device(d)))
else:
    device_dict = _group_device_list(devices)
    num_gpus = None
    for _, devices_in_task in device_dict.items():
        for device_in_task in devices_in_task:
            if num_gpus is None:
                num_gpus = sum(1 for d in device_in_task if _is_gpu_device(d))

            # Verify other workers have the same number of GPUs.
            elif num_gpus != sum(1 for d in device_in_task if _is_gpu_device(d)):
                raise ValueError("All workers should have the same number of GPUs.")

            for d in device_in_task:
                d_spec = tf_device.DeviceSpec.from_string(d)
                if (d_spec.device_type == "GPU" and
                    d_spec.device_index >= num_gpus):
                    raise ValueError("GPU `device_index` on a worker should be "
                                     "consecutive and start from 0.")
    exit(num_gpus)
