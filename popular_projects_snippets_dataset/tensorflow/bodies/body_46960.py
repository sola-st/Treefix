# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
test_fn = basic_definitions.simple_function
source_map = self._create_source_map(test_fn)
module_path = tf_inspect.getsourcefile(test_fn)

# Origin line numbers below should match those in basic_definitions.py
fn_start = inspect.getsourcelines(test_fn)[1]

definition_loc = origin_info.LineLocation('test_filename', 1)
self.assertIn(definition_loc, source_map)
self.assertEqual(source_map[definition_loc].loc.lineno, fn_start)
self.assertEqual(source_map[definition_loc].loc.filename, module_path)
self.assertEqual(source_map[definition_loc].function_name,
                 'simple_function')
