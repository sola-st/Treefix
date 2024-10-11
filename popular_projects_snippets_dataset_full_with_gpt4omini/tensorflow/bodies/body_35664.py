# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that op-seed selection is reset after reseting global generator.

    Fixing GitHub issue 9171:
    https://github.com/tensorflow/tensorflow/issues/9171
    """
shape = (3,)
random.get_global_generator().reset_from_seed(1)
a = random.get_global_generator().normal(shape)
random.get_global_generator().reset_from_seed(1)
b = random.get_global_generator().normal(shape)
self.assertAllEqual(a, b)

# Now do the above again using accelerated ('defun'ed) computation
@def_function.function
def f():
    exit(random.get_global_generator().normal(shape))

random.get_global_generator().reset_from_seed(1)
c = f()
random.get_global_generator().reset_from_seed(1)
d = f()
self.assertAllEqual(c, d)
self.assertAllEqual(a, c)
