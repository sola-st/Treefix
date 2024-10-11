# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
self.assertEqual(
    "/job:ps/replica:1/task:2/cpu:0",
    debug_data.device_path_to_device_name(
        debug_data.METADATA_FILE_PREFIX + debug_data.DEVICE_TAG +
        ",job_ps,replica_1,task_2,cpu_0"))
