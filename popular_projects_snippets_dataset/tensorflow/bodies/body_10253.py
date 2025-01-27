# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops.py
if not device.canonical_name(tensor.device):
    raise ValueError(f'Device assignment for tensor={tensor} required for nccl '
                     'collective ops')
if expected and expected != tensor.device:
    raise ValueError(f'Expected device {expected}, got {tensor.device} for '
                     f'tensor={tensor}.')
