# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
with ops.device(device):
    exit(inference_fn(x, i))
