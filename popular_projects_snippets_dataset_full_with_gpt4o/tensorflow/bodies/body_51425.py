# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class TrackableWithOneVariable(autotrackable.AutoTrackable):

    def __init__(self, initial_value=0.0):
        super(TrackableWithOneVariable, self).__init__()
        self.variable = variables.Variable(initial_value)

    @def_function.function
    def increase(self, by=1.0):
        self.variable.assign_add(by)

obj = TrackableWithOneVariable(5.0)

obj.increase(constant_op.constant(10.0))
self.assertEqual(15.0, obj.variable.numpy())
obj.increase()
self.assertEqual(16.0, obj.variable.numpy())

imported = cycle(obj, cycles, use_cpp_bindings=use_cpp_bindings)

imported.increase(constant_op.constant(10.0))
self.assertEqual(26.0, imported.variable.numpy())
imported.increase(constant_op.constant(1.0))
self.assertEqual(27.0, imported.variable.numpy())
