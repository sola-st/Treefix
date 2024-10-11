# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
input_workers_devices = (("/device:CPU:0", self.worker_devices),)
exit(input_lib.InputWorkers(
    input_workers_devices, canonicalize_devices=False))
