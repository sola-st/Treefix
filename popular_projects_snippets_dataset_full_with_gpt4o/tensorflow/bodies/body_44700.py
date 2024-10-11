# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
# graph-mode iterators are only supported inside tf.function.
@def_function.function(autograph=False)
def test_fn():
    iterator = iter(dataset_ops.Dataset.range(1))
    py_builtins.next_(iterator)
    py_builtins.next_(iterator, constant_op.constant(-3))

# Dataset.range defaults to int64,
with self.assertRaisesRegex(TypeError, 'default.*int64'):
    self.evaluate(test_fn())
