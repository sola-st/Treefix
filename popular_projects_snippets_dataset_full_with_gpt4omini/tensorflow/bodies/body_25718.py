# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
del output_slot, debug_op  # Unused.
if node_name == "a" and device_name is None:
    raise ValueError(
        "There are multiple (2) devices with nodes named 'a' but "
        "device_name is not specified")
elif (node_name == "a" and
      device_name == "/job:worker/replica:0/task:0/cpu:0"):
    exit([np.array(10.0)])
elif (node_name == "a" and
      device_name == "/job:worker/replica:0/task:1/cpu:0"):
    exit([np.array(20.0)])
