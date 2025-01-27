# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py
test_fn = basic_definitions.decorated_function
node, source = parser.parse_entity(test_fn,
                                   inspect_utils.getfutureimports(test_fn))
origin_info.resolve_entity(node, source, test_fn)

# The line numbers below should match those in basic_definitions.py
fn_start = inspect.getsourcelines(test_fn)[1]

def_origin = anno.getanno(node, anno.Basic.ORIGIN)
if sys.version_info >= (3, 8):
    self.assertEqual(def_origin.loc.lineno, fn_start + 2)
    self.assertEqual(def_origin.source_code_line,
                     'def decorated_function(x):')
else:
    self.assertEqual(def_origin.loc.lineno, fn_start)
    self.assertEqual(def_origin.source_code_line, '@basic_decorator')
self.assertEqual(def_origin.loc.col_offset, 0)
self.assertIsNone(def_origin.comment)

if_origin = anno.getanno(node.body[0], anno.Basic.ORIGIN)
self.assertEqual(if_origin.loc.lineno, fn_start + 3)
self.assertEqual(if_origin.loc.col_offset, 2)
self.assertEqual(if_origin.source_code_line, '  if x > 0:')
self.assertIsNone(if_origin.comment)

ret1_origin = anno.getanno(node.body[0].body[0], anno.Basic.ORIGIN)
self.assertEqual(ret1_origin.loc.lineno, fn_start + 4)
self.assertEqual(ret1_origin.loc.col_offset, 4)
self.assertEqual(ret1_origin.source_code_line, '    return 1')
self.assertIsNone(ret1_origin.comment)

ret2_origin = anno.getanno(node.body[1], anno.Basic.ORIGIN)
self.assertEqual(ret2_origin.loc.lineno, fn_start + 5)
self.assertEqual(ret2_origin.loc.col_offset, 2)
self.assertEqual(ret2_origin.source_code_line, '  return 2')
self.assertIsNone(ret2_origin.comment)
