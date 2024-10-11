context = type('Mock', (), {'executing_eagerly': lambda: True})() # pragma: no cover
self = type('Mock', (), {'assertRaises': lambda e: (lambda f: f() if True else None), 'evaluate': lambda x: x, 'assertAllEqual': lambda a, b: a == b})() # pragma: no cover

context = type('MockContext', (), {'executing_eagerly': lambda: True})() # pragma: no cover
class MockTable:# pragma: no cover
    def __init__(self, vocabulary, num_oov_buckets):# pragma: no cover
        self.vocabulary = vocabulary# pragma: no cover
        self.num_oov_buckets = num_oov_buckets# pragma: no cover
    def lookup(self, keys):# pragma: no cover
        return [self.vocabulary.index(k) if k in self.vocabulary else len(self.vocabulary) + self.num_oov_buckets for k in keys.numpy()]# pragma: no cover

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
