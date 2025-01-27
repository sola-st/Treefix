# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def f(x):
    self.assertIsInstance(x, ops.Tensor)
    exit(x)

x = random_ops.random_uniform([2, 2]).numpy()
defined = quarantine.defun_with_attributes(f)
defined(x)
self.assertLen(total_function_cache(defined), 1)

x = random_ops.random_uniform([2, 2]).numpy()
defined(x)
# A NumPy array with different values but the same shape and dtype
# shouldn't trigger another function definition.
self.assertLen(total_function_cache(defined), 1)

np_ones = numpy.ones([], numpy.float32)
np_zeros = numpy.zeros([], numpy.float32)
tf_ones = array_ops.ones([])
tf_zeros = array_ops.zeros([])

# Test that the numpy array is properly an argument to the graph function.
self.assertEqual(1., defined(np_ones).numpy())
self.assertLen(total_function_cache(defined), 2)
self.assertEqual(0., defined(np_zeros).numpy())
self.assertEqual(1., defined(tf_ones).numpy())
self.assertEqual(0., defined(tf_zeros).numpy())
self.assertLen(total_function_cache(defined), 2)

# Test that mutable inputs are supported.
mutable = numpy.ones([], numpy.float32)
self.assertEqual(1., defined(mutable).numpy())
mutable.fill(0)
self.assertEqual(0., defined(mutable).numpy())

class MyNdarray(numpy.ndarray):
    pass

# Test that the subclasses of ndarray are converted too.
self.assertEqual(1., defined(np_ones.view(MyNdarray)).numpy())
self.assertEqual(0., defined(np_zeros.view(MyNdarray)).numpy())

# We should not have triggered any re-tracing of the python function.
self.assertLen(total_function_cache(defined), 2)
