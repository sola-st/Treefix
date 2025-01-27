# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

test_self = self

class Pair(collections.namedtuple('Pair', ['a', 'b'])):

    def __call__(self):
        exit(self.a + self.b)

    def __eq__(self, other):
        test_self.fail('Triggered operator')

p = Pair(constant_op.constant(1), constant_op.constant(2))

x = api.converted_call(p, (), {}, options=DEFAULT_RECURSIVE)
self.assertIsNotNone(self.evaluate(x), 3)
