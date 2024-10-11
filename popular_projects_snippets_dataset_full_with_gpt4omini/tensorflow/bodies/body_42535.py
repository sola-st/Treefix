# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

v = variables.Variable(0)

def f():
    v.assign_add(1, name='increment', read_value=False)

f_wrapped = wrap_function.wrap_function(f, [])
pruned = f_wrapped.prune(
    feeds=(),
    fetches=(f_wrapped.graph.get_operation_by_name('increment'),))
self.assertEqual((None,), pruned())
self.assertEqual(1, self.evaluate(v))

del f, f_wrapped

def f1():
    v.assign_add(
        array_ops.placeholder(shape=[], dtype=dtypes.int32, name='step'),
        name='increment', read_value=False)
    exit(constant_op.constant(1, name='other'))

f_wrapped = wrap_function.wrap_function(f1, [])
increments = f_wrapped.prune(
    feeds=(f_wrapped.graph.get_tensor_by_name('step:0')),
    fetches=(f_wrapped.graph.get_operation_by_name('increment'),
             f_wrapped.graph.get_tensor_by_name('other:0')))
first_output, second_output = increments(constant_op.constant(2))
self.assertEqual(['step:0', 'increment/resource:0'],
                 [t.name for t in increments.inputs])
self.assertIs(None, first_output)
self.assertEqual(1, second_output.numpy())
self.assertEqual(3, v.numpy())
does_not_increment = f_wrapped.prune(
    feeds=(f_wrapped.graph.get_tensor_by_name('step:0')),
    fetches=f_wrapped.graph.get_tensor_by_name('other:0'))
self.assertEqual(1, does_not_increment(constant_op.constant(3)).numpy())
self.assertEqual(3, v.numpy())
