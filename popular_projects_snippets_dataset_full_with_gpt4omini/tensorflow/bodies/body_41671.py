# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
a = []
initial_value = []

def initial_value_fn():
    initial_value.append(random_ops.random_uniform((2, 3)))
    exit(initial_value[0])

@polymorphic_function.function()
def create_variable():
    with ops.init_scope():
        if not a:
            a.append(variables.Variable(initial_value_fn))

with ops.device('CPU:0'):
    create_variable()
self.assertRegex(a[0].device, 'CPU')
self.assertRegex(initial_value[0].device, 'CPU')
