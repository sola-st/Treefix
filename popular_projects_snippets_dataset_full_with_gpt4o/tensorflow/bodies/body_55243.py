# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py
t_stack = traceable_stack.TraceableStack()
t_stack.push_obj(42.0)
t_stack.push_obj('hope')

expected_lifo_peek = ['hope', 42.0]
self.assertEqual(expected_lifo_peek, list(t_stack.peek_objs()))

self.assertEqual('hope', t_stack.pop_obj())
self.assertEqual(42.0, t_stack.pop_obj())
