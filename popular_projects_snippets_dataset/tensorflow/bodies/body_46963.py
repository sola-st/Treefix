# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info_test.py

source = """
      def test_fn(x):
        '''Docstring.'''
        return x  # comment
    """
source = textwrap.dedent(source)
node = parser.parse(source)
origin_info.resolve(node, source, 'test_file', 10, 10)

def_origin = anno.getanno(node, anno.Basic.ORIGIN)
self.assertEqual(def_origin.loc.filename, 'test_file')
self.assertEqual(def_origin.loc.lineno, 10)
self.assertEqual(def_origin.loc.col_offset, 10)
self.assertEqual(def_origin.source_code_line, 'def test_fn(x):')
self.assertIsNone(def_origin.comment)

docstring_origin = anno.getanno(node.body[0], anno.Basic.ORIGIN)
self.assertEqual(def_origin.loc.filename, 'test_file')
self.assertEqual(docstring_origin.loc.lineno, 11)
self.assertEqual(docstring_origin.loc.col_offset, 12)
self.assertEqual(docstring_origin.source_code_line, "  '''Docstring.'''")
self.assertIsNone(docstring_origin.comment)

ret_origin = anno.getanno(node.body[1], anno.Basic.ORIGIN)
self.assertEqual(def_origin.loc.filename, 'test_file')
self.assertEqual(ret_origin.loc.lineno, 12)
self.assertEqual(ret_origin.loc.col_offset, 12)
self.assertEqual(ret_origin.source_code_line, '  return x  # comment')
self.assertEqual(ret_origin.comment, 'comment')
