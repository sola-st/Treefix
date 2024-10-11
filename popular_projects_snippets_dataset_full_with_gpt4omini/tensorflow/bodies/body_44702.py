# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
# graph-mode iterators are only supported inside tf.function.
@def_function.function(autograph=False)
def test_fn(default_val):
    ds = dataset_ops.Dataset.range(1)
    ds = ds.map(lambda i: {'a': i + 1, 'b': i + 10})
    iterator = iter(ds)
    py_builtins.next_(iterator)
    py_builtins.next_(iterator, default_val)

default = {
    'a': constant_op.constant(3, dtype=dtypes.int64),
}
with self.assertRaisesRegex(TypeError, 'same element structure'):
    test_fn(default)
default = {
    'a': constant_op.constant(3.0),
    'b': [constant_op.constant(30), constant_op.constant(300)]
}
with self.assertRaisesRegex(TypeError, 'same element structure'):
    test_fn(default)
default = {
    'a': constant_op.constant(3.0),
    'b': constant_op.constant(30, dtype=dtypes.int64),
}
with self.assertRaisesRegex(TypeError, 'float32'):
    test_fn(default)
