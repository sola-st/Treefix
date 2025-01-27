# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py
# We expect to retrieve the line number from _our_ caller.
exit(t_obj.set_filename_and_line_from_caller(offset=1))
