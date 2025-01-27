# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse(
    textwrap.dedent("""
      def f(a):
        return a + 1
    """))
anno.setanno(node, 'foo', 'bar')
anno.setanno(node, 'baz', 1)
new_node = ast_util.copy_clean(node, preserve_annos={'foo'})
self.assertEqual(anno.getanno(new_node, 'foo'), 'bar')
self.assertFalse(anno.hasanno(new_node, 'baz'))
