# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

v = variables.Variable(0)

def f():
    v.assign(1, read_value=False, name='assign_to_v')

f_wrapped = wrap_function.wrap_function(f, [])
operation_to_fetch = f_wrapped.graph.get_operation_by_name('assign_to_v')
f_pruned = f_wrapped.prune(
    [], operation_to_fetch)
self.assertEqual(
    ['assign_to_v'],
    [operation.name for operation in f_pruned.graph.control_outputs])
self.assertEqual(0, v.numpy())
f_pruned()
self.assertEqual(1, v.numpy())
f_wrapped.prune([], 'assign_to_v')()
f_wrapped.prune([], meta_graph_pb2.TensorInfo(name='assign_to_v'))()
