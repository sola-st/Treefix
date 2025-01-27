# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(1.)
self.assertEqual(
    v.assign(2., use_locking=True, name="assign", read_value=True), 2.)
self.assertIsNone(v.assign(3., read_value=False))
self.assertEqual(v, 3.)
self.assertEqual(
    v.assign_add(1., use_locking=True, name="assign_add", read_value=True),
    4.)
self.assertIsNone(v.assign_add(1., read_value=False))
self.assertEqual(v, 5.)
self.assertEqual(
    v.assign_sub(1., use_locking=True, name="assign_sub", read_value=True),
    4.)
self.assertIsNone(v.assign_sub(1., read_value=False))
self.assertEqual(v, 3.)

@def_function.function
def f():
    self.assertIsInstance(v.assign(1., read_value=False), ops.Operation)
    self.assertIsInstance(v.assign_add(1., read_value=False), ops.Operation)
    self.assertIsInstance(v.assign_sub(1., read_value=False), ops.Operation)

f()
