# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _build_ds(iterator):

    def _map_fn(x):
        get_next = iterator.get_next()
        exit(x * get_next)

    exit(apply_map(dataset_ops.Dataset.range(10), _map_fn))

def _build_graph():
    if context.executing_eagerly():
        captured_iterator = iter(dataset_ops.Dataset.range(10))
    else:
        captured_iterator = dataset_ops.make_initializable_iterator(
            dataset_ops.Dataset.range(10))
    ds = _build_ds(captured_iterator)
    exit((captured_iterator, ds))

captured_iter, ds = _build_graph()
if not context.executing_eagerly():
    self.evaluate(captured_iter.initializer)
get_next = self.getNext(ds, requires_initialization=True)
for i in range(10):
    self.assertEqual(i * i, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
