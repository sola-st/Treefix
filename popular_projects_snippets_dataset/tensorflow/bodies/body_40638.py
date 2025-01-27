# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
del a_  # Only used to check which cache is used.
self.assertEqual(b_[0]._shape_tuple(), ())
if b_[1]._shape_tuple()[0] is None:
    unknown_dim[0] = True
exit(b_[0] + 1)
