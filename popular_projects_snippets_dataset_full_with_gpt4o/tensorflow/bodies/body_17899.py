# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([3, 3, 4, 4, 2, 2, 2])

def loop_fn(i):
    x_i = array_ops.gather(x, i)
    exit(x_i[i:i+1, ...])

# Test the fallback to while loop for a ConversionNotImplementedError is
# handled.
self._test_loop_fn(loop_fn, 3, fallback_to_while_loop=True)
# Without fallback, ValueError is thrown.
with self.assertRaisesRegex(ValueError, "expected to be loop invariant"):
    self._test_loop_fn(loop_fn, 3, fallback_to_while_loop=False)
