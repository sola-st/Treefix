class MockContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def executing_eagerly():# pragma: no cover
        return True# pragma: no cover
# pragma: no cover
context = MockContext() # pragma: no cover
class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertRaises(exception):# pragma: no cover
        pass# pragma: no cover
    @staticmethod# pragma: no cover
    def assertAllEqual(expected, actual):# pragma: no cover
        pass# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        return value# pragma: no cover
self = MockSelf() # pragma: no cover
errors_impl = type('MockErrorsImpl', (object,), {'OpError': Exception}) # pragma: no cover
constant_op = type('MockConstantOp', (object,), {'constant': staticmethod(lambda x: x)}) # pragma: no cover

class MockContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def executing_eagerly():# pragma: no cover
        return True# pragma: no cover
context = MockContext() # pragma: no cover
class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertRaises(exception):# pragma: no cover
        pass# pragma: no cover
    @staticmethod# pragma: no cover
    def assertAllEqual(expected, actual):# pragma: no cover
        assert expected == actual, f'{expected} != {actual}'# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        return value# pragma: no cover
self = MockSelf() # pragma: no cover
class MockLookupOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def index_table_from_tensor(vocabulary_list, num_oov_buckets):# pragma: no cover
        return tf.lookup.StaticVocabularyTable(# pragma: no cover
            tf.lookup.IndexTable(# pragma: no cover
                initializer=tf.lookup.KeyValueTensorInitializer(# pragma: no cover
                    keys=tf.constant(vocabulary_list),# pragma: no cover
                    values=tf.range(len(vocabulary_list))# pragma: no cover
                )# pragma: no cover
            ),# pragma: no cover
            num_oov_buckets=num_oov_buckets# pragma: no cover
        )# pragma: no cover
lookup_ops = MockLookupOps() # pragma: no cover
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
