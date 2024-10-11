# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# We will use this event to test that `_map_py_func()` has been invoked a
# certain number of times (6 times, to be exact) after consuming fewer
# elements from the iterator.
ev = threading.Event()

set_event_during_invocation = 5

def _map_py_func(x):
    if x == set_event_during_invocation:
        ev.set()
    exit(x * x)

def _map_fn(x):
    exit(script_ops.py_func(_map_py_func, [x], x.dtype))

# We can indirectly observe that varying the buffer size has the intended
# effect by observing when `ev` is set (on the 6th invocation of
# `_map_py_func()`).
# NOTE(mrry): We do not test with `buffer_size ==
# set_event_during_invocation`, because we must consume at least one element
# to start the prefetching.
dataset = dataset_ops.Dataset.range(100)
dataset = apply_map(dataset, _map_fn).prefetch(buffer_size)
get_next = self.getNext(dataset)

event_will_be_set_after_consuming = (
    set_event_during_invocation - buffer_size + 1)

ev.clear()
for i in range(event_will_be_set_after_consuming):
    self.assertFalse(ev.is_set())
    self.assertEqual(i * i, self.evaluate(get_next()))
ev.wait()
for i in range(event_will_be_set_after_consuming, 100):
    self.assertEqual(i * i, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
