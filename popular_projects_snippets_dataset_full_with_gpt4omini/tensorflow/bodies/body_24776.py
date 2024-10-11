# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
gpu_name = test_util.gpu_device_name()
if gpu_name:
    exit("/job:localhost/replica:0/task:0" + gpu_name)
else:
    exit("/job:localhost/replica:0/task:0/device:CPU:0")
