context = type('Mock', (object,), {'executing_eagerly': staticmethod(lambda: True)})() # pragma: no cover
self = type('Mock', (object,), {'assertRaises': lambda self, exc: tf.test.TestCase().assertRaises(exc), 'evaluate': lambda self, val: tf.compat.v1.Session().run(val), 'assertAllEqual': lambda self, x, y: tf.test.TestCase().assertAllEqual(x, y)})() # pragma: no cover

context = type('Mock', (object,), {'executing_eagerly': staticmethod(lambda: True)})() # pragma: no cover
self = type('Mock', (object,), {'assertRaises': lambda self, exc: tf.test.TestCase().assertRaises(exc), 'evaluate': lambda self, val: tf.test.TestCase().evaluate(val), 'assertAllEqual': lambda self, x, y: tf.test.TestCase().assertAllEqual(x, y)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
from l3.Runtime import _l_
table = lookup_ops.index_table_from_tensor(
    vocabulary_list=("brain", "salad", "surgery"), num_oov_buckets=1)
_l_(21219)

if not context.executing_eagerly():
    _l_(21223)

    with self.assertRaises(errors_impl.OpError):
        _l_(21221)

        self.evaluate(
            table.lookup(constant_op.constant(("salad", "surgery", "tarkus"))))
        _l_(21220)
else:
    # Reinitializing a table in eager should work.
    table = lookup_ops.index_table_from_tensor(
        vocabulary_list=("brain", "salad", "surgery"), num_oov_buckets=1)
    _l_(21222)
self.evaluate(lookup_ops.tables_initializer())
_l_(21224)
ids = table.lookup(constant_op.constant(("salad", "surgery", "tarkus")))
_l_(21225)
self.assertAllEqual((1, 2, 3), self.evaluate(ids))
_l_(21226)
