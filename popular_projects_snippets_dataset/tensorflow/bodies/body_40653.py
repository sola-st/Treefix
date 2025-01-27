# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def f(**kwargs):
    x = kwargs.pop('x')
    self.assertIsInstance(x, ops.Tensor)
    exit(x)

x = random_ops.random_uniform([2, 2]).numpy()
defined = quarantine.defun_with_attributes(f)
defined(x=x)
self.assertLen(total_function_cache(defined), 1)

x = random_ops.random_uniform([2, 2]).numpy()
defined(x=x)
# A NumPy array with different values but the same shape and dtype
# shouldn't trigger another function definition.
self.assertLen(total_function_cache(defined), 1)

# Test that the numpy array is properly an argument to the graph function.
self.assertEqual(1., defined(x=numpy.ones([])).numpy())
self.assertEqual(0., defined(x=numpy.zeros([])).numpy())
self.assertEqual(1., defined(x=array_ops.ones([])).numpy())
self.assertEqual(0., defined(x=array_ops.zeros([])).numpy())
