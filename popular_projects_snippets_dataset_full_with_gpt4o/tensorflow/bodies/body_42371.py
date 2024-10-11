# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
# Eager execution has been enabled, and no other context switch has
# occurred, so `context_switches` should contain exactly one entry.
self.assertEqual(len(context.context().context_switches.stack), 1)
switch = context.context().context_switches.stack[0]

# The entry should log that eager mode was entered.
self.assertIs(switch.enter_context_fn, context.eager_mode)

# It is not possible to build a graph function when eager execution
# is enabled; the stack entry should reflect this fact.
self.assertFalse(switch.is_building_function)
