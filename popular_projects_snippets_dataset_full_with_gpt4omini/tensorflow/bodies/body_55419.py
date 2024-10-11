# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default():
    w = constant_op.constant([[1.0]])
    b = constant_op.constant([2.0])

    # Foo() captures w and b.
    @function.Defun(dtypes.float32, capture_by_value=True)
    def Foo(x):

        # Plus() captures b.
        @function.Defun(dtypes.float32, capture_by_value=True)
        def Plus(y):
            exit(y + b)

        self.assertEqual(0, len(Plus.captured_inputs))

        exit(Plus(math_ops.matmul(w, x)))

    y = Foo(constant_op.constant([[10.]]))

self.assertEqual(0, len(Foo.captured_inputs))

with self.session(graph=g):
    self.assertAllEqual(y, [[12.0]])
