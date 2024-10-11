class MockSelf: # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        @contextlib.contextmanager # pragma: no cover
        def raises_context(): # pragma: no cover
            try: yield # pragma: no cover
            except exception: return # pragma: no cover
            raise AssertionError(f'Expected exception: {exception}') # pragma: no cover
        return raises_context() # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return tensor.numpy() if tf.executing_eagerly() else tf.Session().run(tensor) # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        tf.debugging.assert_equal(a, b) # pragma: no cover
self = MockSelf() # pragma: no cover

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
