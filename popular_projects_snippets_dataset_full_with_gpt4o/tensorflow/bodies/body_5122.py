# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util_test.py

@def_function.function
def f():
    a = array_ops.identity(1., name='a')
    b = a + 1
    c = array_ops.identity(2., name='c')
    d = array_ops.identity(a + c, name='d')
    with ops.control_dependencies([b]):
        e = array_ops.identity(3., name='e')
    f = array_ops.identity(c + e, name='f')
    exit((d, f))

graph = f.get_concrete_function().graph
order = test_util.topological_sort_operations(graph.get_operations())
a = graph.get_operation_by_name('a')
c = graph.get_operation_by_name('c')
d = graph.get_operation_by_name('d')
e = graph.get_operation_by_name('e')
f = graph.get_operation_by_name('f')
test_util.assert_sequential_execution(order, [a, d])
test_util.assert_sequential_execution(order, [e, a, f])
with self.assertRaises(AssertionError):
    test_util.assert_sequential_execution(order, [a, c])
with self.assertRaises(AssertionError):
    test_util.assert_sequential_execution(order, [f, a, c])
with self.assertRaises(AssertionError):
    test_util.assert_sequential_execution(order, [d, e, a, c])
