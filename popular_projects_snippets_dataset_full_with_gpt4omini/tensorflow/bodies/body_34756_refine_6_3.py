context = type('Mock', (), {'executing_eagerly': lambda: True})() # pragma: no cover
self = type('Mock', (), {'assertRaises': lambda e: (lambda f: f() if True else None), 'evaluate': lambda x: x, 'assertAllEqual': lambda a, b: a == b})() # pragma: no cover

class MockTable:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.vocabulary = ('brain', 'salad', 'surgery')# pragma: no cover
        self.num_oov_buckets = 1# pragma: no cover
    def lookup(self, ids):# pragma: no cover
        return [self.vocabulary.index(id) if id in self.vocabulary else len(self.vocabulary) + self.num_oov_buckets for id in ids.numpy()]# pragma: no cover
# pragma: no cover
lookup_ops = type('MockLookupOps', (object,), {'index_table_from_tensor': lambda vocabulary_list, num_oov: MockTable()})() # pragma: no cover
class MockContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def executing_eagerly():# pragma: no cover
        return True# pragma: no cover
context = MockContext() # pragma: no cover
self = type('MockSelf', (object,), {'assertRaises': lambda e: (lambda f: f()), 'assertAllEqual': lambda a, b: a == b, 'evaluate': lambda x: x})() # pragma: no cover
errors_impl = type('MockErrorsImpl', (object,), {'OpError': Exception}) # pragma: no cover
constant_op = type('MockConstantOp', (object,), {'constant': staticmethod(lambda x: tf.convert_to_tensor(x))}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
from l3.Runtime import _l_
table = lookup_ops.index_table_from_tensor(
    vocabulary_list=("brain", "salad", "surgery"), num_oov_buckets=1)
_l_(8819)

if not context.executing_eagerly():
    _l_(8823)

    with self.assertRaises(errors_impl.OpError):
        _l_(8821)

        self.evaluate(
            table.lookup(constant_op.constant(("salad", "surgery", "tarkus"))))
        _l_(8820)
else:
    # Reinitializing a table in eager should work.
    table = lookup_ops.index_table_from_tensor(
        vocabulary_list=("brain", "salad", "surgery"), num_oov_buckets=1)
    _l_(8822)
self.evaluate(lookup_ops.tables_initializer())
_l_(8824)
ids = table.lookup(constant_op.constant(("salad", "surgery", "tarkus")))
_l_(8825)
self.assertAllEqual((1, 2, 3), self.evaluate(ids))
_l_(8826)
