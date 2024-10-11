# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v1 = variables.Variable(1.0)
v2 = variables.Variable(2.0)
v3 = variables.Variable(4, dtype=dtypes.int32)

trace_count = [0]

@polymorphic_function.function
def double_variable(x):
    trace_count[0] += 1
    x.assign_add(x.read_value())

self.assertEqual(trace_count[0], 0)
double_variable(v1)
self.assertEqual(trace_count[0], 1)
self.assertEqual(self.evaluate(v1), 2.0)
double_variable(v2)
# No retracing because v2's data type and shape are the same as v1
self.assertEqual(trace_count[0], 1)
self.assertEqual(self.evaluate(v2), 4.0)
double_variable(v3)
# Retracing because of data type change
self.assertEqual(trace_count[0], 2)
self.assertEqual(self.evaluate(v3), 8)
