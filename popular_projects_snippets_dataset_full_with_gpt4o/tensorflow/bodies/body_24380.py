# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
if test.is_gpu_available():
    cls._expected_partition_graph_count = 2
    cls._expected_num_devices = 2
    gpu_name = test_util.gpu_device_name()
    cls._main_device = "/job:localhost/replica:0/task:0" + gpu_name
else:
    cls._expected_partition_graph_count = 1
    cls._expected_num_devices = 1
    cls._main_device = "/job:localhost/replica:0/task:0/device:CPU:0"
