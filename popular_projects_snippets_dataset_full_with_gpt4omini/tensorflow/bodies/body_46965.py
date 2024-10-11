# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
test_fn = basic_definitions.simple_function
node, source = parser.parse_entity(
    test_fn, inspect_utils.getfutureimports(test_fn))
origin_info.resolve_entity(node, source, test_fn)

# The line numbers below should match those in basic_definitions.py
fn_start = inspect.getsourcelines(test_fn)[1]

def_origin = anno.getanno(node, anno.Basic.ORIGIN)
self.assertEqual(def_origin.loc.lineno, fn_start)
self.assertEqual(def_origin.loc.col_offset, 0)
self.assertEqual(def_origin.source_code_line, 'def simple_function(x):')
self.assertIsNone(def_origin.comment)

docstring_origin = anno.getanno(node.body[0], anno.Basic.ORIGIN)
self.assertEqual(docstring_origin.loc.lineno, fn_start + 1)
self.assertEqual(docstring_origin.loc.col_offset, 2)
self.assertEqual(docstring_origin.source_code_line, '  """Docstring."""')
self.assertIsNone(docstring_origin.comment)

ret_origin = anno.getanno(node.body[1], anno.Basic.ORIGIN)
self.assertEqual(ret_origin.loc.lineno, fn_start + 2)
self.assertEqual(ret_origin.loc.col_offset, 2)
self.assertEqual(ret_origin.source_code_line, '  return x  # comment')
self.assertEqual(ret_origin.comment, 'comment')
