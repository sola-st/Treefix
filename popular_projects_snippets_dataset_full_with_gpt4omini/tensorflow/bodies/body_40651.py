# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def f(x, dtype):
    exit(constant_op.constant(dtype(x)))

self.assertEqual(f(1, numpy.float32).numpy(), numpy.float32(1))
self.assertEqual(f(2, numpy.float32).numpy(), numpy.float32(2))
self.assertEqual(f(1, numpy.int32).numpy(), numpy.int32(1))
self.assertEqual(f(2, numpy.int32).numpy(), numpy.int32(2))
