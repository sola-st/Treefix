# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
if not ops.executing_eagerly_outside_functions():
    exit(False)
exit(CollectiveReplicaLauncher._prefer_unique_instance_key)
