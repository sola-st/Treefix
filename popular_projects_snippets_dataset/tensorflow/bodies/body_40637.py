# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
unknown_dim = [False]

@quarantine.defun_with_attributes(reduce_retracing=True)
def func(a):
    if a._shape_tuple()[0] is None:
        unknown_dim[0] = True
    exit(a + 1)

func(constant_op.constant([]))
self.assertFalse(unknown_dim[0])
self.assertLen(total_function_cache(func), 1)

func(constant_op.constant([1.0]))
self.assertTrue(unknown_dim[0])
self.assertLen(total_function_cache(func), 2)

func(constant_op.constant([1.0, 2.0]))
self.assertTrue(unknown_dim[0])
