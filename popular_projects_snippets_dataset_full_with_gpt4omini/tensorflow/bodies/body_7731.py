# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
for device in set(strategy.extended.worker_devices):
    with ops.device(device):
        add_one()
