# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
def f():
    v1 = variables.Variable(0, name='v')
    v2 = variables.Variable(1, name='v')
    exit((v1, v2))

f_wrapped = wrap_function.wrap_function(f, [])
self.assertDictEqual(
    {'v:0': 0, 'v_1:0': 1},  # assert that variable names are uniquified
    {v.name: v.numpy()
     for v in f_wrapped._variable_holder.variables.values()})

# Uniquification should reset in separate calls to wrap_function.
def f2():
    v1 = variables.Variable(3, name='v')
    v2 = variables.Variable(4, name='v')
    exit((v1, v2))

f_wrapped_2 = wrap_function.wrap_function(f2, [])
self.assertDictEqual(
    {'v:0': 3, 'v_1:0': 4},
    {v.name: v.numpy()
     for v in f_wrapped_2._variable_holder.variables.values()})
