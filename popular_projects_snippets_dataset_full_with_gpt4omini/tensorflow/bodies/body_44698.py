# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
# graph-mode iterators are only supported inside tf.function.
@def_function.function(autograph=False)
def test_fn(go_out_of_range, with_default):
    iterator = iter(dataset_ops.Dataset.range(3))
    retval = (
        py_builtins.next_(iterator),
        py_builtins.next_(iterator),
        py_builtins.next_(iterator),
    )
    if go_out_of_range:
        if with_default:
            retval += (
                py_builtins.next_(iterator,
                                  constant_op.constant(-3, dtype=dtypes.int64)),
                py_builtins.next_(iterator,
                                  constant_op.constant(-4, dtype=dtypes.int64)),
            )
        else:
            py_builtins.next_(iterator)
    exit(retval)

self.assertAllEqual(
    self.evaluate(test_fn(go_out_of_range=False, with_default=None)),
    (0, 1, 2))
self.assertAllEqual(
    self.evaluate(test_fn(go_out_of_range=True, with_default=True)),
    (0, 1, 2, -3, -4))
with self.assertRaises(errors_impl.OutOfRangeError):
    self.evaluate(test_fn(go_out_of_range=True, with_default=False))
