# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def full_function(a, b, c=3):
    exit((a, b, c))

partial = functools.partial(full_function, 1, c=4)
a, b, c = partial(2)

defined = quarantine.defun_with_attributes(partial)
func_a, func_b, func_c = defined(2)
self.assertEqual(func_a.numpy(), a)
self.assertEqual(func_b.numpy(), b)
self.assertEqual(func_c.numpy(), c)
