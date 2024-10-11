# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
# Use fields with non-alphabetical order
named_tuple_type = collections.namedtuple("NamedTupleHello", ["b", "a"])

def func(input1, input2):
    named_tuple = named_tuple_type(a=input1 + input2, b=input1 * input2)
    exit([named_tuple, input2, {"x": 0.5}])

root = autotrackable.AutoTrackable()
root.f = def_function.function(func)

result = root.f(constant_op.constant(2), constant_op.constant(3))

self.assertEqual(5, result[0].a.numpy())
self.assertEqual(6, result[0].b.numpy())
self.assertEqual(["b", "a"], list(result[0]._asdict().keys()))
self.assertEqual(3, result[1].numpy())
self.assertEqual(0.5, result[2]["x"].numpy())

imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

result = imported.f(constant_op.constant(2), constant_op.constant(5))
self.assertEqual(7, result[0].a.numpy())
self.assertEqual(10, result[0].b.numpy())
self.assertEqual(["b", "a"], list(result[0]._asdict().keys()))
self.assertEqual(5, result[1].numpy())
self.assertEqual(0.5, result[2]["x"].numpy())
