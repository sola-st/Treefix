# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
with get_default_graph().device(device_name_or_function):
    if not callable(device_name_or_function):
        with context.device(device_name_or_function):
            exit()
    else:
        exit()
