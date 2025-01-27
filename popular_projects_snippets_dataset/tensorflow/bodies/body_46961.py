# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
test_fn = basic_definitions.function_with_multiline_call
source_map = self._create_source_map(test_fn)
module_path = tf_inspect.getsourcefile(test_fn)

# Origin line numbers below should match those in basic_definitions.py
fn_start = inspect.getsourcelines(test_fn)[1]

call_loc = origin_info.LineLocation('test_filename', 3)
self.assertIn(call_loc, source_map)
self.assertEqual(source_map[call_loc].loc.lineno, fn_start + 2)
self.assertEqual(source_map[call_loc].loc.filename, module_path)
self.assertEqual(source_map[call_loc].function_name,
                 'function_with_multiline_call')
self.assertEqual(source_map[call_loc].source_code_line, '  return range(')

second_arg_loc = origin_info.LineLocation('test_filename', 5)
self.assertIn(second_arg_loc, source_map)
self.assertEqual(source_map[second_arg_loc].loc.lineno, fn_start + 4)
self.assertEqual(source_map[second_arg_loc].loc.filename, module_path)
self.assertEqual(source_map[second_arg_loc].function_name,
                 'function_with_multiline_call')
self.assertEqual(source_map[second_arg_loc].source_code_line,
                 '      x + 1,')
