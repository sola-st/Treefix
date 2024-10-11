self = type('Mock', (), {'assertRaises': staticmethod(lambda *args: None), 'assertAllEqual': staticmethod(lambda *args: None), 'evaluate': staticmethod(lambda x: x)})() # pragma: no cover

class MockContext:# pragma: no cover
    @staticmethod# pragma: no cover
    def executing_eagerly():# pragma: no cover
        return False# pragma: no cover
context = MockContext() # pragma: no cover
class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertRaises(exception, func):# pragma: no cover
        try:# pragma: no cover
            func()# pragma: no cover
        except exception:# pragma: no cover
            pass# pragma: no cover
    @staticmethod# pragma: no cover
    def assertAllEqual(a, b):# pragma: no cover
        assert a == b, f'{a} != {b}'# pragma: no cover
    @staticmethod# pragma: no cover
    def evaluate(x):# pragma: no cover
        return x# pragma: no cover
self = MockSelf() # pragma: no cover
def mock_index_table_from_tensor(vocabulary_list, num_oov_buckets):# pragma: no cover
    class MockTable:# pragma: no cover
        def lookup(self, x):# pragma: no cover
            return tf.constant([1 if item == 'salad' else 2 if item == 'surgery' else 3 for item in x.numpy()])# pragma: no cover
    return MockTable()# pragma: no cover

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
