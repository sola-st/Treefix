# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py
t_stack = traceable_stack.TraceableStack()

# We expect that the line number recorded for the 1-object will come from
# the call to t_stack.push_obj(1).  Do not separate the next two lines!
placeholder_1 = lambda x: x
t_stack.push_obj(1)

# We expect that the line number recorded for the 2-object will come from
# the call to call_push_obj() and _not_ the call to t_stack.push_obj().
def call_push_obj(obj):
    t_stack.push_obj(obj, offset=1)

# Do not separate the next two lines!
placeholder_2 = lambda x: x
call_push_obj(2)

expected_lineno_1 = inspect.getsourcelines(placeholder_1)[1] + 1
expected_lineno_2 = inspect.getsourcelines(placeholder_2)[1] + 1

t_obj_2, t_obj_1 = t_stack.peek_traceable_objs()
self.assertEqual(expected_lineno_2, t_obj_2.lineno)
self.assertEqual(expected_lineno_1, t_obj_1.lineno)
