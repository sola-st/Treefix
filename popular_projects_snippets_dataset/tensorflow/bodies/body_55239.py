# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py
t_obj = traceable_stack.TraceableObject(17)

# Do not separate placeholder from the set_filename_and_line_from_caller()
# call one line below it as it is used to calculate the latter's line
# number.
placeholder = lambda x: x
result = t_obj.set_filename_and_line_from_caller()

expected_lineno = inspect.getsourcelines(placeholder)[1] + 1
self.assertEqual(expected_lineno, t_obj.lineno)
self.assertEqual(_THIS_FILENAME, t_obj.filename)
self.assertEqual(t_obj.SUCCESS, result)
