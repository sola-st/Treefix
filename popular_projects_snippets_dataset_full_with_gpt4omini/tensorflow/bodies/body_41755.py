# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f():
    func = lambda: x
    # TODO(b/263520817): Remove access to private attribute.
    exit(ops.get_default_graph(
        )._function_captures._create_capture_placeholder(func))

x = {
    'tensor': constant_op.constant(0),
    'list': [constant_op.constant(1), 2],
    'dict': {
        'float': constant_op.constant(0.5)
    }
}

out = f()
# tf.function output should have same structure/values with the side input
self.assertEqual(x['tensor'].numpy(), out['tensor'].numpy())
self.assertEqual(x['list'][0].numpy(), out['list'][0].numpy())
self.assertEqual(x['list'][1], out['list'][1].numpy())
self.assertEqual(x['dict']['float'].numpy(), out['dict']['float'].numpy())
