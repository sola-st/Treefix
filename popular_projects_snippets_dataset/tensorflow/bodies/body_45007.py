# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

l = lambda x: x == 0

x = api.converted_call(
    l, (constant_op.constant(0),), None, options=DEFAULT_RECURSIVE)

self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(True, self.evaluate(x))
