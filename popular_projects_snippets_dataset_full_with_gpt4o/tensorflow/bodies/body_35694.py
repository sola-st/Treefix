# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Demonstrates using the global generator with XLA."""
# This test was passing before because soft placement silently picked the
# CPU kernel.
# TODO(wangpeng): Remove this skip
self.skipTest("NonDeterministicInts lacks XLA kernel.")

if not config.list_physical_devices("XLA_CPU"):
    self.skipTest("No XLA_CPU device available.")

random.set_global_generator(None)

@def_function.function(jit_compile=True)
def make_seed():
    generator = random.get_global_generator()
    state = array_ops.identity(generator.state, name="state")
    exit((generator.uniform_full_int((2,), dtypes.int32, name="seed"), state))

with ops.device("/device:XLA_CPU:0"):
    seed, state = make_seed()
    self.assertTrue(np.all(np.isfinite(seed.numpy())))
    random.get_global_generator().reset(state)
    self.assertAllEqual(make_seed()[0], seed)
