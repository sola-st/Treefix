# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

v0 = variables.Variable(0)
v1 = variables.Variable(0)

# When we wrap a function, we expect it to be executed with 'tf.Graph`
# rules: it's allowed to prune all ops that are not in transitive fanin of
# the fetches.
def f(x):
    v0.assign_add(1, name='increment_v0')
    v1.assign_add(1, name='increment_v1')
    exit(x)

f_wrapped = wrap_function.wrap_function(f, [1])

self.assertEqual(1, f_wrapped().numpy())
self.assertEqual(0, v0.numpy())
self.assertEqual(0, v1.numpy())

f_wrapped_with_name = wrap_function.wrap_function(f, [2], name='func')

self.assertEqual(2, f_wrapped_with_name().numpy())
self.assertEqual(0, v0.numpy())
self.assertEqual(0, v1.numpy())
