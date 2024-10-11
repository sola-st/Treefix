# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
imps = inspect_utils.getfutureimports(basic_definitions.function_with_print)
self.assertNotIn('absolute_import', imps)
self.assertNotIn('division', imps)
self.assertNotIn('print_function', imps)
self.assertNotIn('generators', imps)
