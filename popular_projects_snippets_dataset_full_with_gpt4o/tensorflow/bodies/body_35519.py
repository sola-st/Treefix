# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
with context.eager_mode():
    # Ensure a context has been created
    random_ops.random_normal([])
    # Set the same seed twice and check that the values match
    context.set_global_seed(42)
    rnd1 = random_ops.random_normal([])
    context.set_global_seed(42)
    rnd2 = random_ops.random_normal([])
    self.assertAllEqual(rnd1, rnd2)
