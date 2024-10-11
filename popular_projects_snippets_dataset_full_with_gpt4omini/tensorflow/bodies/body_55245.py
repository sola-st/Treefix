# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py
t_stack = traceable_stack.TraceableStack()
t_stack.push_obj(0)
t_stack.push_obj(1)
t_stack.push_obj(2)
t_stack.push_obj(3)

obj_3 = t_stack.pop_obj()
obj_2 = t_stack.pop_obj()
obj_1 = t_stack.pop_obj()
obj_0 = t_stack.pop_obj()

self.assertEqual(3, obj_3)
self.assertEqual(2, obj_2)
self.assertEqual(1, obj_1)
self.assertEqual(0, obj_0)
