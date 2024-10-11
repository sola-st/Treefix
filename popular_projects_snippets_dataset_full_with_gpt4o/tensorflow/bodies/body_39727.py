# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
"""Benchmark overheads of creating a Tensor object."""
if device == GPU:
    # Warmup the GPU
    ops.EagerTensor(value, device=device)

def func():
    ops.EagerTensor(value, device=device, dtype=dtype)

self._run(func, 30000)
