class MockContext(object):# pragma: no cover
    def executing_eagerly(self):# pragma: no cover
        return True# pragma: no cover
context = MockContext() # pragma: no cover
class MockSelf(object):# pragma: no cover
    def assertRaises(self, *args, **kwargs):# pragma: no cover
        return contextlib.ExitStack()# pragma: no cover
    def assertAllEqual(self, x, y):# pragma: no cover
        assert x == y# pragma: no cover
self = MockSelf() # pragma: no cover
class MockErrorsImpl(object):# pragma: no cover
    class OpError(Exception):# pragma: no cover
        pass# pragma: no cover
errors_impl = MockErrorsImpl() # pragma: no cover

class MockContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def executing_eagerly():# pragma: no cover
        return True# pragma: no cover
context = MockContext() # pragma: no cover
class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertRaises(exception, func):# pragma: no cover
        try:# pragma: no cover
            func()# pragma: no cover
        except exception:# pragma: no cover
            pass# pragma: no cover
    @staticmethod# pragma: no cover
    def evaluate(value):# pragma: no cover
        return value# pragma: no cover
    @staticmethod# pragma: no cover
    def assertAllEqual(expected, actual):# pragma: no cover
        assert expected == actual, f'{expected} != {actual}'# pragma: no cover
self = MockSelf() # pragma: no cover
class MockTable:# pragma: no cover
    def __init__(self, vocabulary_list, num_oov_buckets):# pragma: no cover
        self.vocabulary_list = vocabulary_list# pragma: no cover
        self.num_oov_buckets = num_oov_buckets# pragma: no cover
    def lookup(self, ids):# pragma: no cover
        return [self.vocabulary_list.index(id) if id in self.vocabulary_list else self.num_oov_buckets for id in ids.numpy()]# pragma: no cover

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
