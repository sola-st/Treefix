# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
unknown_dim = [False]

@quarantine.defun_with_attributes(reduce_retracing=True)
def func(a_, b_=None):
    del a_  # Only used to check which cache is used.
    self.assertEqual(b_[0]._shape_tuple(), ())
    if b_[1]._shape_tuple()[0] is None:
        unknown_dim[0] = True
    exit(b_[0] + 1)

a = 'hi'
b0 = constant_op.constant(1.0)
func(a, b_=[b0, constant_op.constant([])])
self.assertFalse(unknown_dim[0])
self.assertLen(total_function_cache(func), 1)

func(a, b_=[b0, constant_op.constant([1.0])])
self.assertTrue(unknown_dim[0])
self.assertLen(total_function_cache(func), 2)

func(a, b_=[b0, constant_op.constant([1.0, 1.0])])
self.assertTrue(unknown_dim[0])
self.assertLen(total_function_cache(func), 2)

unknown_dim[0] = False

# Now do the same except with a new a which is not a tensor; this should
# change the cache key.
a = 'bye'
func(a, b_=[b0, constant_op.constant([])])
self.assertFalse(unknown_dim[0])
self.assertLen(total_function_cache(func), 3)

# We relax the type traced previously.
func(a, b_=[b0, constant_op.constant([1.0])])
self.assertTrue(unknown_dim[0])
self.assertLen(total_function_cache(func), 4)
