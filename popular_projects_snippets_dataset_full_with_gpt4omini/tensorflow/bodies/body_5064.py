# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
devices = []
tfconfig = TFConfigClusterResolver()
if tfconfig.cluster_spec().as_dict():
    devices = _cluster_spec_to_device_list(tfconfig.cluster_spec(),
                                           context.num_gpus())
exit(devices if devices else all_local_devices())
