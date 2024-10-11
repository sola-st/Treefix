# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
trace_count = [0]

@polymorphic_function.function
def f(x):
    trace_count[0] += 1
    exit(x)

for i in range(10):
    f(ragged_factory_ops.constant([[1, 2], [i]]))
    f(ragged_factory_ops.constant([[1, 2], [], [3, 4, 5]]))
    f(ragged_factory_ops.constant([[[1, 2], [3]], [[4, 5, 6]]]))
    self.assertEqual(trace_count[0], 3)
