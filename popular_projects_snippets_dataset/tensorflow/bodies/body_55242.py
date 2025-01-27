# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack_test.py
t_obj = traceable_stack.TraceableObject('The quick brown fox.')
# This line shouldn't die.
result = t_obj.set_filename_and_line_from_caller(offset=300)

# We expect a heuristic to be used because we are not currently 300 frames
# down on the stack.  The filename and lineno of the outermost frame are not
# predictable -- in some environments the filename is this test file, but in
# other environments it is not (e.g. due to a test runner calling this
# file).  Therefore we only test that the called function knows it applied a
# heuristic for the ridiculous stack offset.
self.assertEqual(t_obj.HEURISTIC_USED, result)
