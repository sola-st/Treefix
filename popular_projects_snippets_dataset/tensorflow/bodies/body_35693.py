# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
generator = random.get_global_generator()
state = array_ops.identity(generator.state, name="state")
exit((generator.uniform_full_int((2,), dtypes.int32, name="seed"), state))
