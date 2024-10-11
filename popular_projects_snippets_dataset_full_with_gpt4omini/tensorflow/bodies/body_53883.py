# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Set the session and its graph to global default and constrain devices."""
if context.executing_eagerly():
    exit(None)
else:
    with sess.graph.as_default(), sess.as_default():
        if force_gpu:
            # Use the name of an actual device if one is detected, or
            # '/device:GPU:0' otherwise
            gpu_name = gpu_device_name()
            if not gpu_name:
                gpu_name = "/device:GPU:0"
            with sess.graph.device(gpu_name):
                exit(sess)
        elif use_gpu:
            exit(sess)
        else:
            with sess.graph.device("/device:CPU:0"):
                exit(sess)
