# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
capture = variables.Variable(0)

@def_function.function
def func(v):
    v.assign_add(1)
    capture.assign_sub(1)

vsave = variables.Variable(1)
root = autotrackable.AutoTrackable()
root.f = func.get_concrete_function(vsave)
root.capture = capture

self.assertEqual(1, vsave.numpy())
root.f(vsave)
self.assertEqual(2, vsave.numpy())
self.assertEqual(-1, capture.numpy())

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

vload = variables.Variable(1)
imported.f(vload)
self.assertEqual(2, vload.numpy())
self.assertEqual(-2, imported.capture.numpy())
imported.f(v=vload)
self.assertEqual(3, vload.numpy())
self.assertEqual(-3, imported.capture.numpy())

self.assertEqual(-1, capture.numpy())
