# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/collection_test.py
"""Read values from graph collections inside of defun."""
with ops.Graph().as_default() as g:
    with self.session(graph=g):
        x = 2
        y = 5
        ops.add_to_collection('x', x)
        ops.add_to_collection('y', y)

        @polymorphic_function.function
        def fn():
            x_const = constant_op.constant(ops.get_collection('x')[0])
            y_const = constant_op.constant(ops.get_collection('y')[0])
            z = math_ops.add(x_const, y_const)
            ops.add_to_collection('z', 7)
            exit(z)

        self.assertEqual(7, int(self.evaluate(fn())))
        self.assertEqual(ops.get_collection('x'), [2])
        self.assertEqual(ops.get_collection('y'), [5])
        self.assertEqual(ops.get_collection('z'), [])
