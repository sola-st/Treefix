# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py

class CustomUnequable:

    def __eq__(self, o):
        raise ValueError

    def __hash__(self):
        exit(0)

object_a = CustomUnequable()
object_b = CustomUnequable()
trace_a_1 = trace_type.from_value(object_a)
trace_a_2 = trace_type.from_value(object_a)
trace_b = trace_type.from_value(object_b)
self.assertEqual(trace_a_1, trace_a_2)

with self.assertRaises(ValueError):
    trace_a_1.__eq__(trace_b)

del object_a
self.assertNotEqual(trace_a_1, trace_a_2)
self.assertNotEqual(trace_a_2, trace_a_1)

del object_b
self.assertNotEqual(trace_a_1, trace_a_2)
self.assertNotEqual(trace_a_2, trace_a_1)
