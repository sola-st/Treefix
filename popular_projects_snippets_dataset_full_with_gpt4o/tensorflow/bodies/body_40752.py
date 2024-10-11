# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def defined(t):
    exit(t)

defined(array_ops.zeros([12, 1]))
self.assertLen(total_function_cache(defined), 1)
defined(array_ops.zeros([1, 21]))
self.assertLen(total_function_cache(defined), 2)

@quarantine.defun_with_attributes
def defined_again(t):
    exit(defined(t))

defined_again.get_concrete_function(array_ops.zeros([12, 1]))
self.assertLen(total_function_cache(defined_again), 1)
defined_again.get_concrete_function(array_ops.zeros([1, 21]))
self.assertLen(total_function_cache(defined_again), 2)
