# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
# File name with too few underscores should lead to an exception.
device_dir = os.path.join(
    self._dump_root,
    debug_data.METADATA_FILE_PREFIX + debug_data.DEVICE_TAG +
    ",job_localhost,replica_0,task_0,cpu_0")
os.makedirs(device_dir)
open(os.path.join(device_dir, "node1_DebugIdentity_1234"), "wb")

with self.assertRaisesRegex(ValueError,
                            "does not conform to the naming pattern"):
    debug_data.DebugDumpDir(self._dump_root)
