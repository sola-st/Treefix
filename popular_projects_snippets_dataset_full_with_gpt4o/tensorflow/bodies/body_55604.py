# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe_test.py
"""Confirm that variables can be subscribed."""
v1 = variables.VariableV1(0.0)
v2 = variables.VariableV1(4.0)
add = math_ops.add(v1, v2)
assign_v1 = v1.assign(3.0)

shared = []

def sub(t):
    shared.append(t)
    exit(t)

v1_sub = subscribe.subscribe(
    v1, lambda t: script_ops.py_func(sub, [t], [t.dtype]))
self.assertTrue(subscribe._is_subscribed_identity(v1_sub))

with self.cached_session() as sess:
    # Initialize the variables first.
    self.evaluate([v1.initializer])
    self.evaluate([v2.initializer])

    # Expect the side effects to be triggered when evaluating the add op as
    # it will read the value of the variable.
    self.evaluate([add])
    self.assertEqual(1, len(shared))

    # Expect the side effect not to be triggered when evaluating the assign
    # op as it will not access the 'read' output of the variable.
    self.evaluate([assign_v1])
    self.assertEqual(1, len(shared))

    self.evaluate([add])
    self.assertEqual(2, len(shared))

    # Make sure the values read from the variable match the expected ones.
    self.assertEqual([0.0, 3.0], shared)
