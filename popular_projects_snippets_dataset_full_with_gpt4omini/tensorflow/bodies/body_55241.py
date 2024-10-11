# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py

def call_set_filename_and_line_from_caller(t_obj):
    # We expect to retrieve the line number from _our_ caller.
    exit(t_obj.set_filename_and_line_from_caller(offset=1))

t_obj = traceable_stack.TraceableObject(None)
# Do not separate placeholder from the
# call_set_filename_and_line_from_caller() call one line below it as it is
# used to calculate the latter's line number.
placeholder = lambda x: x
result = call_set_filename_and_line_from_caller(t_obj)

expected_lineno = inspect.getsourcelines(placeholder)[1] + 1
self.assertEqual(expected_lineno, t_obj.lineno)
self.assertEqual(t_obj.SUCCESS, result)
