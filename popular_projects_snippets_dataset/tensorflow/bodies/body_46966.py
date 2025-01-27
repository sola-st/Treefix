# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
test_fn = basic_definitions.nested_functions
node, source = parser.parse_entity(
    test_fn, inspect_utils.getfutureimports(test_fn))
origin_info.resolve_entity(node, source, test_fn)

# The line numbers below should match those in basic_definitions.py
fn_start = inspect.getsourcelines(test_fn)[1]

inner_def_origin = anno.getanno(node.body[1], anno.Basic.ORIGIN)
self.assertEqual(inner_def_origin.loc.lineno, fn_start + 3)
self.assertEqual(inner_def_origin.loc.col_offset, 2)
self.assertEqual(inner_def_origin.source_code_line, '  def inner_fn(y):')
self.assertIsNone(inner_def_origin.comment)

inner_ret_origin = anno.getanno(node.body[1].body[0], anno.Basic.ORIGIN)
self.assertEqual(inner_ret_origin.loc.lineno, fn_start + 4)
self.assertEqual(inner_ret_origin.loc.col_offset, 4)
self.assertEqual(inner_ret_origin.source_code_line, '    return y')
self.assertIsNone(inner_ret_origin.comment)
