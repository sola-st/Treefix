self = type('Mock', (object,), {})() # pragma: no cover
self.assertRaises = staticmethod(lambda exc_type, func: None) # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover
self.assertAllEqual = lambda a, b: a == b # pragma: no cover

class MockContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def executing_eagerly():# pragma: no cover
        return True# pragma: no cover
context = MockContext() # pragma: no cover
class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertRaises(exception, func):# pragma: no cover
        pass# pragma: no cover
    def assertAllEqual(self, expected, actual):# pragma: no cover
        assert expected == actual# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        return value# pragma: no cover
self = MockSelf() # pragma: no cover
lookup_ops = type('MockLookupOps', (object,), {# pragma: no cover
        'index_table_from_tensor': staticmethod(lambda vocabulary_list, num_oov_buckets:# pragma: no cover
            type('MockTable', (object,), {# pragma: no cover
                'lookup': lambda self, x: [# pragma: no cover
                    vocabulary_list.index(i) if i in vocabulary_list else (len(vocabulary_list) + num_oov_buckets)# pragma: no cover
                    for i in x.numpy()# pragma: no cover
                ]# pragma: no cover
            })()# pragma: no cover
        ),# pragma: no cover
        'tables_initializer': staticmethod(lambda: None)# pragma: no cover
    }) # pragma: no cover
constant_op = type('MockConstantOp', (object,), {'constant': staticmethod(lambda x: tf.convert_to_tensor(x))}) # pragma: no cover
errors_impl = type('MockErrorsImpl', (object,), {'OpError': Exception}) # pragma: no cover

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
