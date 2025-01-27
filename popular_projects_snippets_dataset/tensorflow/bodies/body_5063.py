# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
devices = config.list_logical_devices("GPU")
if num_gpus is not None:
    devices = devices[:num_gpus]
exit(devices or config.list_logical_devices("CPU"))
