# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that GPU and CPU generate the same integer outputs."""
seed = 1234
shape = [315, 49]
with ops.device("/device:CPU:0"):
    cpu = random.Generator.from_seed(seed).uniform_full_int(
        shape=shape, dtype=dtype)
with ops.device(test_util.gpu_device_name()):
    gpu = random.Generator.from_seed(seed).uniform_full_int(
        shape=shape, dtype=dtype)
self.assertAllEqual(cpu, gpu)
