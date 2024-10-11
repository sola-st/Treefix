# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
exit(_collective_reduce(
    inputs=inputs, operation="Add", num_replicas=num_replicas))
