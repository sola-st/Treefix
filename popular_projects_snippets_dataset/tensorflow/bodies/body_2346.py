# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Tests XLA and CPU kernels generate the same integers in overflow case.

       Specifically this tests the case where the counter is incremented past
       what can fit within 64 bits of the 128 bit Philox counter.
    """
dtype = dtypes.uint64
seed = 2**64 - 10
shape = [315, 49]
with ops.device("/device:CPU:0"):
    cpu_gen = random.Generator.from_seed(seed=seed, alg=random.RNG_ALG_PHILOX)
with ops.device(xla_device_name()):
    xla_gen = random.Generator.from_seed(seed=seed, alg=random.RNG_ALG_PHILOX)
# Repeat multiple times to make sure that the state after
# number-generation are the same between CPU and XLA.
for _ in range(5):
    with ops.device("/device:CPU:0"):
        # Test both number-generation and skip
        cpu = cpu_gen.uniform_full_int(shape=shape, dtype=dtype)
        cpu_gen.skip(100)
    with ops.device(xla_device_name()):
        xla = xla_gen.uniform_full_int(shape=shape, dtype=dtype)
        xla_gen.skip(100)
    self.assertAllEqual(cpu, xla)
    self.assertAllEqual(cpu_gen.state, xla_gen.state)
self.assertAllEqual(cpu, xla)
