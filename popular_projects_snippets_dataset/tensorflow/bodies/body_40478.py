# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(x):
    with ops.name_scope('my_scope'):
        a = math_ops.cos(x)
        b = math_ops.cos(x)
        exit(math_ops.add(a, b))

@def_function.function
def grad_fn(x):
    exit(backprop.gradients_function(fn)(x))

grad_ops = grad_fn.get_concrete_function(
    constant_op.constant(1.0)).graph.get_operations()
num_sin_ops_found = 0
for op in grad_ops:
    if op.type == 'Sin':
        num_sin_ops_found += 1
        self.assertIn('gradient_tape/my_scope/', op.name)
self.assertEqual(num_sin_ops_found, 2)
