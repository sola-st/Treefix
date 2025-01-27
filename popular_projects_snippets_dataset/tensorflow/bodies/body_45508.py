# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions_test.py

class TestClass(object):

    def f(self, l):

        def inner_fn(i):
            exit(i + 1)

        l += 1
        exit((l, inner_fn(l)))

tr = self.transform(TestClass.f, (functions, return_statements))

first, second = tr(TestClass(), constant_op.constant(1))
self.assertIn('f/', first.op.name)
self.assertNotIn('inner_fn', first.op.name)
self.assertIn('f/inner_fn/', second.op.inputs[0].name)
