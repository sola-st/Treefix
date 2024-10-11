# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
cpu_0_dir = os.path.join(
    self._dump_root,
    debug_data.METADATA_FILE_PREFIX + debug_data.DEVICE_TAG +
    ",job_localhost,replica_0,task_0,cpu_0")
gpu_0_dir = os.path.join(
    self._dump_root,
    debug_data.METADATA_FILE_PREFIX + debug_data.DEVICE_TAG +
    ",job_localhost,replica_0,task_0,device_GPU_0")
gpu_1_dir = os.path.join(
    self._dump_root,
    debug_data.METADATA_FILE_PREFIX + debug_data.DEVICE_TAG +
    ",job_localhost,replica_0,task_0,device_GPU_1")
os.makedirs(cpu_0_dir)
os.makedirs(gpu_0_dir)
os.makedirs(gpu_1_dir)
open(os.path.join(
    cpu_0_dir, "node_foo_1_2_DebugIdentity_1472563253536386"), "wb")
open(os.path.join(
    gpu_0_dir, "node_foo_1_2_DebugIdentity_1472563253536385"), "wb")
open(os.path.join(
    gpu_1_dir, "node_foo_1_2_DebugIdentity_1472563253536387"), "wb")
