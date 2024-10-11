# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Confirm that supported types are correctly detected and handled."""

a = constant_op.constant(1)
b = constant_op.constant(1)
c = math_ops.add(a, b)

def sub(t):
    exit(t)

# Tuples.
subscribed = subscribe.subscribe(
    (a, b), lambda t: script_ops.py_func(sub, [t], [t.dtype]))
self.assertIsInstance(subscribed, tuple)
self._ExpectSubscribedIdentities(subscribed)

# Lists.
subscribed = subscribe.subscribe(
    [a, b], lambda t: script_ops.py_func(sub, [t], [t.dtype]))
self.assertIsInstance(subscribed, list)
self._ExpectSubscribedIdentities(subscribed)

# Dictionaries.
subscribed = subscribe.subscribe({
    'first': a,
    'second': b
}, lambda t: script_ops.py_func(sub, [t], [t.dtype]))
self.assertIsInstance(subscribed, dict)
self._ExpectSubscribedIdentities(subscribed.values())

# Namedtuples.
# pylint: disable=invalid-name
TensorPair = collections.namedtuple('TensorPair', ['first', 'second'])
# pylint: enable=invalid-name
pair = TensorPair(a, b)
subscribed = subscribe.subscribe(
    pair, lambda t: script_ops.py_func(sub, [t], [t.dtype]))
self.assertIsInstance(subscribed, TensorPair)
self._ExpectSubscribedIdentities(subscribed)

# Expect an exception to be raised for unsupported types.
with self.assertRaisesRegex(TypeError, 'has invalid type'):
    subscribe.subscribe(c.name,
                        lambda t: script_ops.py_func(sub, [t], [t.dtype]))
