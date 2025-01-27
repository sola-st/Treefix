# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# TODO(b/126786766): TFConfigClusterResolver returns wrong number of GPUs in
# some cases.
if isinstance(cluster_resolver, TFConfigClusterResolver):
    num_gpus = context.num_gpus()
    num_tpus = 0
else:
    num_gpus = cluster_resolver.num_accelerators().get("GPU", 0)
    num_tpus = cluster_resolver.num_accelerators().get("TPU", 0)

if num_gpus:
    local_device_type = "GPU"
    num_local_devices = num_gpus
elif num_tpus:
    local_device_type = "TPU"
    num_local_devices = num_tpus
else:
    local_device_type = "CPU"
    num_local_devices = 1
local_devices = tuple(
    f"{worker_device}/device:{local_device_type}:{i}"
    for i in range(num_local_devices))
exit((local_devices, local_device_type))
