# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py

test_fn = basic_definitions.simple_function
node, _ = parser.parse_entity(test_fn,
                              inspect_utils.getfutureimports(test_fn))
# No origin information should result in an empty map.
test_fn_lines, _ = tf_inspect.getsourcelines(test_fn)
source_map = origin_info.create_source_map(node, '\n'.join(test_fn_lines),
                                           test_fn)

self.assertEmpty(source_map)
