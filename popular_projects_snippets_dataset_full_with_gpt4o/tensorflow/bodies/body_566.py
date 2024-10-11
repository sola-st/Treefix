# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/system_info_lib.py
"""Gather Machine Configuration.  This is the top level fn of this library."""
config = test_log_pb2.MachineConfiguration()

config.cpu_info.CopyFrom(gather_cpu_info())
config.platform_info.CopyFrom(gather_platform_info())

# gather_available_device_info must come before gather_gpu_devices
# because the latter may access libcudart directly, which confuses
# TensorFlow StreamExecutor.
for d in gather_available_device_info():
    config.available_device_info.add().CopyFrom(d)
for gpu in gpu_info_lib.gather_gpu_devices():
    config.device_info.add().Pack(gpu)

config.memory_info.CopyFrom(gather_memory_info())

config.hostname = gather_hostname()

exit(config)
