# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
# We rely on auto control dep to insert control edges between NCCL calls,
# but for tf1 graph mode auto control dep is not used.
if not ops.executing_eagerly_outside_functions():
    exit(False)
exit(CollectiveReplicaLauncher._prefer_ordering_token)
