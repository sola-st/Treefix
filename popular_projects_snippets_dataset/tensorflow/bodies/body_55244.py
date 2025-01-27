# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py
t_stack = traceable_stack.TraceableStack()
t_stack.push_obj(42.0)
t_stack.push_obj('hope')
self.assertEqual('hope', t_stack.peek_top_obj())
