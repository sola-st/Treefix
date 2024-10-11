# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse(
    textwrap.dedent("""
      def f(a):
        return a + 1
    """))
setattr(node, '__foo', 'bar')
new_node = ast_util.copy_clean(node)
self.assertIsNot(new_node, node)
self.assertFalse(hasattr(new_node, '__foo'))
